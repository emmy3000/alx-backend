#!/usr/bin/node
/*
  Script: 0-redis_client.js

  Description:
  This script uses the 'redis' package to connect to a Redis server.
  It logs a success message to the console when the connection is established
  and an error message when the connection fails.
*/

import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err.message}`);
});
