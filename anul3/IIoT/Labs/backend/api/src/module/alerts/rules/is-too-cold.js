const sensorEnum = require('../../sensors.enum');

const name = (location) => `Temperature is too low in '${location}'`;
const description = (timestamp, temperature) => `From a sensor reading at ${timestamp}, the temperature is ${temperature} degrees Celsius which is too low for this location animals.`;
const temperatureThreshold = 10;

module.exports = async (allAlerts, NotificationModel, location) => {
    const readings = allAlerts.filter((reading) =>
        reading.type === sensorEnum.TEMPERATURE_SENSOR 
        && Math.floor(Date.now()) - new Date(reading.timestamp).getTime() < 3 * 60 * 1000
        && reading.value < temperatureThreshold
    );

    // we want at least 2 readings in the last 3 minutes
    if (readings.length < 2) {
        return false;
    }

    const notification = new NotificationModel({
        name: name(location),
        // we want always the latest reading
        description: description(readings[0].timestamp, readings[0].value),
        sensorReadings: readings.map((reading) => reading._id),
    });

    await notification.save();
    return true;
}