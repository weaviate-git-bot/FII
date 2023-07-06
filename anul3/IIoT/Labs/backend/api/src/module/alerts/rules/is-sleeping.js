const sensorEnum = require('../../sensors.enum');

const name = (location) => `Animal in '${location}' is sleeping`;
const description = (timestamp, avgTilt) => `From a sensor reading at ${timestamp}, the tilt sensor haven't reached the movement threshold in the last 5 minutes. (Avg: ${avgTilt})`;
const tiltThreshold = 700;

module.exports = async (allAlerts, NotificationModel, location) => {
    const readings = allAlerts.filter((reading) =>
        reading.type === sensorEnum.TILT_SENSOR
        // if in the last 5 minutes there was a tilt sensor reading
        && Math.floor(Date.now()) - new Date(reading.timestamp).getTime() < 5 * 60 * 1000
        && reading.value < tiltThreshold
    );

    // we want at least 3 readings in the last 5 minutes
    if (readings.length < 3) {
        return false;
    }

    const avgReading = readings.reduce((acc, reading) => acc + reading.value, 0) / readings.length;

    const notification = new NotificationModel({
        name: name(location),
        // we want always the latest reading
        description: description(readings[0].timestamp, avgReading),
        sensorReadings: readings.map((reading) => reading._id),
    });

    await notification.save();
    return true;
}