const sensorEnum = require('../../sensors.enum');

const name = (location) => `Animal can't hydrate properly in '${location}'`;
const description = (timestamp) => `From a sensor reading at ${timestamp}, the temperature and moisture sensor indicate that the animal can't hydrate properly. (Temperature high, moisture low)`;
const temperatureThreshold = 30;
const moistureThreshold = 500;

module.exports = async (allAlerts, NotificationModel, location) => {
    const readings = allAlerts.filter((reading) =>
        (reading.type === sensorEnum.TEMPERATURE_SENSOR || reading.type === sensorEnum.SOIL_MOISTURE_SENSOR)
        // if in the last 5 minutes there was a tilt sensor reading
        && Math.floor(Date.now()) - new Date(reading.timestamp).getTime() < 5 * 60 * 1000
        && (reading.value > temperatureThreshold || reading.value < moistureThreshold)
    );

    // we want at least 3 readings in the last 5 minutes
    if (readings.length < 3) {
        return false;
    }


    const notification = new NotificationModel({
        name: name(location),
        // we want always the latest reading
        description: description(readings[0].timestamp),
        sensorReadings: readings.map((reading) => reading._id),
    });

    await notification.save();
    return true;
}