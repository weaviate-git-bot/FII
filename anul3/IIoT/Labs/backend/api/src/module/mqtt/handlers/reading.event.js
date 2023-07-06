const ReadingsSchema = require('../../../models/reading.model');

const handleReadingEvent = async (topic, message) => {
    const { timestamp, location } = message;
    await Promise.all(message.data.map(async (value) => {
        const reading = new ReadingsSchema({
            type: value.sensor_id,
            value: value.value,
            timestamp,
            location
        });
        await reading.save();
    }));
    return null;
}

module.exports = handleReadingEvent