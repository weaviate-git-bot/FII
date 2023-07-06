const express = require('express');
const router = express.Router();
const notificationsController = require('../controller/notifications.controller');

router.get(
    '/notifications',
    notificationsController.getAllNotifications
);
  

module.exports = router;
