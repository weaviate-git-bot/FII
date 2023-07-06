const mqtt = require('mqtt')
const config = require('../config')
const alerts = require('../alerts');
const handlers = require('./handlers');

const options = {
    host: config.mqtt.host,
    port: 8883,
    protocol: 'mqtts',
    username: config.mqtt.username,
    password: config.mqtt.password
}

// initialize the MQTT client
const client = mqtt.connect(options);

const handleOnReceiveMessage = async (topic, message) => {
    try {
        const msg = JSON.parse(message.toString());
        
        const response = await handlers[msg.event_type](topic, msg);
        
        if (response) {
            client.publish(`uaic/response/${topic.split('uaic/')[1]}`, JSON.stringify(response));
        }

        console.log('Successfully processed message received on topic: ', topic);
        // this will be processed async and will not block the main thread
        alerts.onEvent(msg.location);
    } catch(err) {
        console.log(`Failed to process message received on topic: ${topic}. Error: ${err}`);
    }
}

// setup the callbacks
client.on('connect', function () {
    console.log('Connected to MQTT broker');
});

client.on('error', function (error) {
    console.log('Failed to read data.',error);
});

client.on('message', handleOnReceiveMessage);

client.subscribe('uaic/savana/#');