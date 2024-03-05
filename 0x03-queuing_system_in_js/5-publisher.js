// Connects to the Redis server and
// logs a message when the connection is successful or not

const redis = require('redis');

const client = redis.createClient();

client.on('connect', () => {
    console.log('Redis client connected to the server');
    });

client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err.message}`);
    }
);

// Publish a message after a given time
const publishMessage = (message, time) => {
    setTimeout(() => {
        console.log(`About to send ${message}`);
        client.publish('holberton school channel', message);
    }, time);
}

publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
