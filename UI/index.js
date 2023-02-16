const express = require('express')
const mqtt = require('mqtt')
const path = require('path');
const { json } = require('express');
const bodyParser = require('body-parser');
const util = require('util');
const fs = require('fs');
const app = express()
const port = 3000

const readFile = util.promisify(fs.readFile);
app.use(bodyParser.json());
function read(filePath = './devices.json') {
    return readFile(path.resolve(__dirname, filePath)).then(data => JSON.parse(data));
}
const options = {
    host: 'bec3bbc6c9c44b4fae7e5a42781338c5.s2.eu.hivemq.cloud',
    port: 8883,
    protocol: 'mqtts',
    username: 'tester',
    password: '12345678'
}
const client = mqtt.connect(options);
var topic = "Phuong/LED";
client.on('connect', function () {
    console.log("connected!");
    client.subscribe(topic);
});

app.get('/', async (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});
app.get('/devices', async (req, res) => {
    const devices = await read();
    res.json(devices);
});

app.post('/',function(req,res) {
    const topic = req.body.topic;
    const msg = req.body.msg;
    //client.publish(topic, msg);
    console.log(topic + " value:"+ msg);
    client.publish(topic, msg);
    res.sendStatus(200);
});

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})