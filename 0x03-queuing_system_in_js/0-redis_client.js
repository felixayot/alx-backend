// Connects to the Redis server and:
// - Logs to the console the message Redis client connected to the server
//   when the connection to Redis works correctly
// - Log to the console the message Redis client not connected to the server:
//   ERROR_MESSAGE when the connection to Redis does not work

const redis = require('redis');

const client = redis.createClient();

client.on('connect', () => {
    console.log('Redis client connected to the server');
    });

client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err.message}`);
    }
);

// module.exports = client;
