# IIoT Homework

### Minimal configuration:
- [x] Motion Sensors
- [x] Smoke sensors
- [x] Webcam
- [x] Smart Doors
- [x] Smart Windows
- [x] Garage Door
- [x] Ventilator comandat de termostat
- [x] Sirena antiefractie
- [x] Stropitoare gazon
- [x] Umidometru

- conectivitate Wifi (done), Bluetooth (done), RFID (done)
- manageriere faciala (prin smartphone si laptop) <--- sper sa mearga vrajeala cu license plate reader
- actuatori si senzori programati (done)
- sistemul sa cuprinda atat senzori cat si actuatori care folosesc protocolul TCP/IP (done) si senzori care folosesc un controller (arduino - done)

### First Floor
#### All rooms will have the following configuration:
- MCU Board with 4 Temperature Sensors AC & Furnace connection 
	- based on the 3 inside temperature sensors readings it will open or close the AC 
	- based on the inside and outside temperature sensor it will open or close the Furnace 

- MCU board with 2 sensors (1x Smoke Sensor, 1x Humidity Sensor) and 3 outputs (1x Siren, 1x Humidifier, 1x Ceiling Sprinkle) 
	- based on the smoke sensor readings (if it exceeds 45% it will start the alarm and the ceiling sprinkle)
	- based on humidity sensors (value < 35 ) it will start the humidity sensor until it reaches 70

#### Kitchen 
Configuration
- 1x Smart Window (ip: 192.168.2.23)
- 1x Ceiling Fan (ip: 192.168.2.25)
- 1x Carbon Dioxide Sensor (ip: 192.168.2.27)
- 1x Carbon Monoxide Sensor (ip: 192.168.2.29)

Kitchen Logic:

- if Monoxide Sensor or Carbon Dioxide sensor have value >= 50 or the alarm on one of the is triggered set the Ceiling Fan to High and open the Window
- close the Window and Ceiling fan if Monoxide Sensor or Carbon Dioxide Sensor read values lower then 10
- set the Ceiling fan to sensor when the value of Monoxide Sensor or Carbon Dioxide  <= 20

### Entrance

We have an Access Point (SSID: MainEntranceAP01) that covers all entrances and garage door

These Access Point it's on the same sub-network as the Configuration Server (ip: 192.168.2.7) and the default gateway for this subnet is 192.167.2.5 

All the components (except on those we specially mention, are connected to the Configuration Server via the AccessPoint)

#### Main entrance
Components:
- 1x RFID Reader (ip: 192.168.2.9)
- 1x RFID Card (id: 1001) (doesn't support wirless connection, it's a card)
- 1x Smart Door (ip: 192.168.2.11)

Entrance logic:

- when we tap an RFID Card to the RFID Reader we validate that the ID is on the allowed list
- if it's on the allowed list we unlock the door
- else we keep the door locked
- when the RFID Reader stops reading the card, after a small delay we lock the door

#### Garage entrance
Components:
- 1x Webcam (ip: 192.168.2.13)
- 1x Motion Detector Sensor (outside) (ip: 192.168.2.15)
- 1x Smart Garage Door (ip: 192.168.2.17)
- 1x Motion Detector Sensor (inside) (ip: 192.168.2.21)

Garage logic:
1. a car enters the garage path and the Outside Motion Detector gets triggered
2. when the Outside Motion Detector it's triggered, we open the Webcam to read the car's license plate
3. if we get a match, the garage door open
4. the Inside Motion Detector sensor starts reading.
5. the Garage Door closes when the Inside Motion Detector sensor stops reading


#### Main hallway
Components:
- 3x Motion Detection Sensor
	- MD01 ip: 192.168.2.41
	- MD02 ip: 192.168.2.43
	- MD03 ip: 192.168.2.45
-4x Light
	- LeftLamp01 ip: 192.168.2.47
	- LeftLamp02 ip: 192.168.2.49
	- RightLamp03 ip: 192.168.2.51
	- RightLamp04 ip: 192.168.2.53

Logic:
1. Someone enters the Main hallway
2. if it's picked up by MD01 it will trigger LeftLamp01 and LeftLamp02
3. if it's picked up by MD02 it will trigger LeftLamp02 and RightLamp03
4. if it's picked up by MD03 it will trigger RightLamp04
5. the close sequence is the natural one

### Second Floor

Components:
- 1x Thermostat
- 1x Fan
- 1x Furnace
- 1x MCU-PT

Logic:
1. if the thermostat writes to D2 we start the Fan on High
2. if the thermostat stops writing to D2 we stop the fan
3. if the thermostat writes to D1 we start the Furnace
4. if the thermostat stops writing to D1 we stop the Thermostat
5. if the thermostat has 0 on both D1 and D2 we stop everything

### User network

All user devices (e.g Laptop, Smartphone, PCs) are connected to a different subnet, handled by HomeRouter PT-AC (SSID: YoyoHomeWifi5.2) 
with default gateway to 192.168.3.5

- BZV Room laptop (ip: 192.168.3.11)
- BZV Room smartphone (ip: 192.168.3.105)
- Radu Room laptop (ip: 192.168.3.13)
- Work Room printer (ip: 192.168.3.15)
- Studio Room Portable Music Player (ip: 192.168.3.107)

### Studio room
Components:
- Studio Room Portable Music Player (ip: 192.168.3.107)
- 2x Bluetooth Speaker (connected via Bluetooth)

Logic:
1. Activate Portable Music Player

### Garden

Components:
- 5x Floor Sprinkle
- 4x Humiture Sensor

Logic:
- if any humiture sensor reads below 50 -> start all sprinkles
- if all humiture sensor are above 75 -> stop all strinkles
- if avg humiture is 65 -> start all sprinkles

## Source codes
AC/Furnance based on temperature
```python
#!/usr/bin/env python3
from time import sleep
from gpio import *

def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)

def get_avg_temp(pins):
	temps = 0
	
	for p in pins:
		reading = analogRead(p)
		temps += translate(reading, 0, 1023, -100,100)
		
	return temps / len(pins)

def main():
	AC_PIN = 0
	FURNACE_PIN = 1
	pinMode(AC_PIN, OUTPUT)
	pinMode(FURNACE_PIN, OUTPUT)
	inside_sensors = [A0, A2, A3]
	outside_sensors = [A1]
	acStatus = 0
	furnaceStatus = 0

	while True:
		inside_temperature = get_avg_temp(inside_sensors)
		outside_temperature = get_avg_temp(outside_sensors)
		
		if inside_temperature > 27 and acStatus == 0:
			digitalWrite(AC_PIN, HIGH)
			acStatus = 1
			print("Turing on AC")
			
		if (inside_temperature < 20 and outside_temperature < 10) and furnaceStatus == 0:
			furnaceStatus = 1
			digitalWrite(FURNACE_PIN, HIGH)
			print("Turing on Furnace")
			
		if inside_temperature <= 23 and acStatus == 1:
			digitalWrite(AC_PIN, LOW)
			acStatus = 0
			print("Turing off AC")
		
		if inside_temperature >= 23 and furnaceStatus == 1:
			furnaceStatus = 0
			digitalWrite(FURNACE_PIN, LOW)
			print("Turing off Furnace")
		
		print("Inside temp:", inside_temperature)	
		sleep(5)
	
if __name__ == '__main__':
    main()
```

Smoke/Humidity sensors
```python
#!/usr/bin/env python3
from time import sleep
from gpio import *

HUMIDITY_SENSOR_PIN = A0 # analog
SMOKE_SENSOR_PIN =  A1 #analog
SPRINKLE_PIN = 0 #output
HUMIDIFIER_PIN = 1 #output
SIRENE_PIN = 2 #output

def translate(x, in_min, in_max, out_min, out_max):
  return ((x - in_min) * (out_max - out_min)) // (in_max - in_min) + out_min
  
  
def read_and_translate(pin):
	sensor = analogRead(pin)
	return translate(sensor, 0, 1023, 0, 100)

def main():
	humidifier_status = 0
	sirene_status = 0
	
	pinMode(HUMIDIFIER_PIN, OUTPUT)
	pinMode(SIRENE_PIN, OUTPUT)
	
	while True:
		smoke_sensor = read_and_translate(SMOKE_SENSOR_PIN)
		humitidy_sensor = read_and_translate(HUMIDITY_SENSOR_PIN)
		
		if smoke_sensor > 60 and sirene_status == 0:
			digitalWrite(SIRENE_PIN, HIGH)
			sirene_status = 1
			print("Starting Sirene")
		
		if smoke_sensor <= 30 and sirene_status == 1:
			sirene_status = 0
			digitalWrite(SIRENE_PIN, LOW)
			print("Stopping sirene")
			
		if humitidy_sensor < 45 and humidifier_status == 0:
			digitalWrite(HUMIDIFIER_PIN, HIGH)
			humidifier_status = 1
			print("Starting humidifier")
		
		if humitidy_sensor > 65 and humidifier_status == 1:
			digitalWrite(HUMIDIFIER_PIN, LOW)
			humidifier_status = 0
			print("Stoping humidifier")
		
		sleep(1.0)

if __name__ == '__main__':
    main()
```

Thermostat controlling a Fan
```python
#!/usr/bin/env python3
from time import sleep
from gpio import *

FURNACE_SENSOR_PIN = 1 # in
AC_SENSOR_PIN =  2 #in
FAN_PIN = 0 #output
FURNACE_PIN = 3 # output

def main():
	fan_status = 0
	furnace_status = 0
	
	pinMode(FAN_PIN, OUTPUT)
	pinMode(FURNACE_PIN, OUTPUT)
	
	while True:
		shouldHeat = digitalRead(FURNACE_SENSOR_PIN)
		shouldCool = digitalRead(AC_SENSOR_PIN)
		print(shouldHeat, shouldCool)
		if shouldCool != 0 and fan_status == 0:
			customWrite(FAN_PIN, "2")
			fan_status = 2
			print("Starting fan on position 2")
		
		if shouldCool == 0 and fan_status != 0:
			customWrite(FAN_PIN, "0")
			print("Stopping fan")
			fan_status = 0
		
		if shouldHeat != 0 and furnace_status == 0:
			print("starting furnace")
			digitalWrite(FURNACE_PIN, HIGH)
			furnace_status = 1
		
		if shouldHeat == 0 and furnace_status == 1:
			print("stopping furnace")
			digitalWrite(FURNACE_PIN, LOW)
			furnace_status = 0
	
		
		sleep(5.0)

if __name__ == '__main__':
    main()
```

Sprinkle Control
```python
#!/usr/bin/env python3
from time import sleep
from gpio import *

HUMITURE_SENSOR_PINS = [0, 1, 2, 3]
FLOOR_SPRINKLES = [1, 2, 3, 4, 5]

def translate(x, in_min, in_max, out_min, out_max):
  return ((x - in_min) * (out_max - out_min)) // (in_max - in_min) + out_min
  
  
def read_and_translate(pin):
	sensor = analogRead(pin)
	return translate(sensor, 0, 1023, 0, 100)

def avg(list_data):
	sum = 0
	for x in list_data:
		sum += x
	
	return sum / len(list_data)

def read_data():
	data = []
	for humitureSensor in HUMITURE_SENSOR_PINS:
		data.append(read_and_translate(humitureSensor))
	
	print("Minimul value, Avg value", data, min(data), avg(data))
	
	if avg(data) == 0:
		return LOW
	
	if min(data) < 50:
		return HIGH

	if avg(data) < 65:
		return HIGH

	if avg(data) > 75:
		return LOW

	return LOW

def main():
	fan_status = 0
	furnace_status = 0
	
	for floorSprinkles in FLOOR_SPRINKLES:
		pinMode(floorSprinkles, OUTPUT)
	
	while True:
		data = read_data()

		for floorSprinkles in FLOOR_SPRINKLES:
			digitalWrite(floorSprinkles, data)
		
		sleep(5.0)

if __name__ == '__main__':
    main()
```

