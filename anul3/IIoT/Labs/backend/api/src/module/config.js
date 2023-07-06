const dotenv = require('dotenv');

let config = null;


const loadConfig = () => {
    if (config !== null) {
        return config;
    }
    const loadedConfig = dotenv.config().parsed
    config = {
        port: parseInt(loadedConfig.PORT || '1337', 10),
        mongoUri: loadedConfig.MONGO_URI,
        mqtt: {
            host: loadedConfig.MQTT_HOST,
            port: parseInt(loadedConfig.MQTT_PORT || '8883', 10),
            username: loadedConfig.MQTT_USERNAME,
            password: loadedConfig.MQTT_PASSWORD
        }
    }
    return config;
}

module.exports = loadConfig();