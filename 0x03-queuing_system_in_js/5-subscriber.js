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

client.subscribe('holberton school channel');
client.on('message', (channel, message) => {
    console.log(message);
    if (message === 'KILL_SERVER') {
        client.unsubscribe(channel);
        client.quit();
    }
});
