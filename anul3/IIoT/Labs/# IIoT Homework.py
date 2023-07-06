# IIoT Homework

### First Floor

All rooms will have the following configuration:
- MCU Board with 4 Temperature Sensors AC & Furnance connection

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
	pinMode(0, OUTPUT)
	pinMode(1, OUTPUT)
	inside_sensors = [A0, A2, A3]
	outside_sensors = [A1]
	acStatus = 0
	furnaceStatus = 0

	while True:
		inside_temperature = get_avg_temp(inside_sensors)
		outside_temperature = get_avg_temp(outside_sensors)
		
		if inside_temperature > 27 and acStatus == 0:
			digitalWrite(0, HIGH)
			acStatus = 1
			print("Turing on AC")
			
		if inside_temperature < 20 and furnaceStatus == 0:
			furnaceStatus = 1
			digitalWrite(1, HIGH)
			print("Turing on Furnace")
			
		if inside_temperature <= 23 and acStatus == 1:
			digitalWrite(0, LOW)
			acStatus = 0
			print("Turing off AC")
		
		if inside_temperature >= 23 and furnaceStatus == 1:
			furnaceStatus = 0
			digitalWrite(1, LOW)
			print("Turing off Furnace")
		
		print("Inside temp:", inside_temperature)	
		sleep(5)
	
if __name__ == '__main__':
    main()
```