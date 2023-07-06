const Notification = require("../models/notification.model");

exports.getAllNotifications = async (req, res, next) => {
    try {
        const notifications = await Notification.find({}).sort({ createdAt: -1 }).populate('sensorReadings');
        res.status(200).json({
            message: "All notifications fetched successfully",
            data: notifications,
        });
    } catch (err) {
        next(err);
    }
}