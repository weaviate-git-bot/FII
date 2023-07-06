const ReadingsSchema = require('../../models/reading.model');
const NotificationModel = require('../../models/notification.model');
const rules = require('./rules');

// you can access data up to 3 days (because there are lots of readings)
const maximumAlertTimeDifference = 72 * 60 * 60 * 1000;

exports.onEvent = async (location) => {
    console.log('[ALERTS] Event received for location:', location);
    const allAlerts = await ReadingsSchema.find({ location, timestamp: {
        $gte: new Date(new Date().getTime() - maximumAlertTimeDifference)
    } }).sort({ timestamp: -1 })
    const rulesResponse = await Promise.all(rules.map((rule) => rule(allAlerts, NotificationModel, location)));
    const addedAtLeastOneRule = rulesResponse.some((rule) => rule);

    if (addedAtLeastOneRule) {
        console.log('[ALERTS] Added at least one rule using the alert from location: ', location);
    }
}