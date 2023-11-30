#!/usr/bin/node
/*
  Script: 1-redis_op.js

  Description:
  This script uses the 'redis' package to connect to a Redis server.
  It includes two additional functions: setNewSchool and displaySchoolValue.
*/

import redis from 'redis';

const client = redis.createClient();

// Display a message when the Redis client connects
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Display a message if there is an error connecting to Redis
client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err.message}`);
});

// Function to set a new school value in Redis
const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, redis.print);
};

// Function to display the value for a given school in Redis
const displaySchoolValue = (schoolName) => {
  client.get(schoolName, (err, reply) => {
    console.log(reply);
  });
};

// Call functions as specified
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
