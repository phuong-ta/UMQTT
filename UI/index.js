const mqtt = require('mqtt')

var options = {
    host: '<your cloud>',
    port: 8883,
    protocol: 'mqtts',
    username: '<your user name>',
    password: '<your password>'
}
var client = mqtt.connect(options); 

// connect, then publish message to broker with LED info
client.on('connect', function () {
  client.subscribe('Phuong/LED', function (err) {
    if (!err) {
      client.publish('Phuong/LED', 'D3;40%') // 
    }
  })
})

// check that did message send sucessfully
client.on('message', function (topic, message) {
  // message is Buffer
  console.log(message.toString())
  client.end()
})