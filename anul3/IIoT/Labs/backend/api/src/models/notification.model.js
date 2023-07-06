const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const NotificationSchema = new Schema({
  name: {
    type: String,
    required: true,
  },
  description: {
    type: String,
    required: true,
  },
  sensorReadings: [{
    type: Schema.Types.ObjectId,
    ref: 'sensor_readings',
  }],
  createdAt: {
    type: Date,
    required: true,
    default: Date.now,
  }
});

const NotificationModel = mongoose.model('notifications', NotificationSchema);
module.exports = NotificationModel;
