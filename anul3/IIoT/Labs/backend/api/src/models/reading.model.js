const mongoose = require("mongoose");
const sensorsEnum = require("../module/sensors.enum");
const Schema = mongoose.Schema;

const ReadingsSchema = new Schema({
  type: {
    type: Number,
    required: true,
    enum: Object.keys(sensorsEnum).map((key) => sensorsEnum[key]),
  },
  value: {
    type: Number,
    required: true,
  },
  timestamp: {
    type: Date,
    required: true,
    default: Date.now,
  },
  location: {
    type: String,
    required: true,
  }
}, {
  toJSON: {
    virtuals: true,
  },
});

ReadingsSchema.virtual('name').get(function () {
  try {
    return {
      1: 'Soil Moisture',
      2: 'Temperature',
      3: 'Tilt',
    }[this.type];
  } catch (err) {
    return 'Unknown';
  }
});

const SensorsModel = mongoose.model("sensor_readings", ReadingsSchema);


module.exports = SensorsModel;
