#!/usr/bin/node
/*
  Script: 4-redis_advanced_op.js

  Description:
  This script uses the 'redis' package to connect to a Redis server
  and performs advanced operations using hash values.

  Create Hash:
  The script uses hset to store a hash value with the key HolbertonSchools
  and values for different cities.

  Display Hash:
  The script uses hgetall to display the object stored in Redis.

  Requirements:
  - Use callbacks for the operations.

  How to run:
  bob@dylan:~$ npm run dev 4-redis_advanced_op.js
*/

import { createClient } from 'redis';

// Create a Redis client
const client = createClient();

// Event handler for connection errors
client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

// Function to create hash using hset
const createHash = (hashName, data, callback) => {
  const entries = Object.entries(data);

  function setHashEntry([field, value]) {
    client.hset(hashName, field, value, (err, reply) => {
      console.log(`Reply: ${reply}`);
      if (entries.length) {
        setHashEntry(entries.shift());
      } else {
        callback();
      }
    });
  }

  setHashEntry(entries.shift());
};

// Function to display hash using hgetall
const displayHash = (hashName) => {
  client.hgetall(hashName, (err, obj) => {
    console.log(obj);
    // Close the Redis connection
    client.quit();
  });
};

// Data for creating the hash
const hashData = {
  'Portland': 50,
  'Seattle': 80,
  'New York': 20,
  'Bogota': 20,
  'Cali': 40,
  'Paris': 2,
};

// Create and display the hash
createHash('HolbertonSchools', hashData, () => {
  displayHash('HolbertonSchools');
});
