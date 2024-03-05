// Connects to the Redis server and
// logs a message when the connection is successful or not

const redis = require('redis');
const promisify = require('util').promisify;

const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);

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

// Gets from Redis the value for the key schoolName asynchronously
async function displaySchoolValue(schoolName) {
    console.log(await getAsync(schoolName));
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
