const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const config = require('./module/config');
const mqttListener = require('./module/mqtt');
const cors = require('cors');

mongoose.connect(config.mongoUri, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
});
const routes = require('./routes');

const app = express();
app.use(cors({
    origin: 'http://localhost:3000',
}));
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());
app.use('/', routes);
app.use((err, req, res, next) => {
    const statusCode = err.statusCode || 500;
    res.status(statusCode);
    res.json({
        success: false,
        message: 'Request has failed',
        error: {
            statusCode: statusCode,
            message: err.message,
        },
    });
})

app.listen(config.port, () => console.log('IIoT backend server listening on port 1336!'));