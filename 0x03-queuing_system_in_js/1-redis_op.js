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

// Sets in Redis the value for the key schoolName
// and displays a confirmation message using redis.print
const setNewSchool = (schoolName, value) => {
    client.set(schoolName, value, redis.print);
}

// Gets from Redis the value for the key schoolName
const displaySchoolValue = (schoolName) => {
    client.get(schoolName, (err, reply) => {
        console.log(reply);
    });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
