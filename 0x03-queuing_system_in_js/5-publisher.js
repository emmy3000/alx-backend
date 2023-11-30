#!/usr/bin/node
/*
  Script: 5-publisher.js

  Description:
  This script creates a Redis publisher client that connects to a Redis server.
  It publishes messages to the channel "holberton school channel" with specified delays.
  The messages are logged to the console before being published.

  Requirements:
  - Use the 'redis' package.
  - Run with Node.js.

  How to run:
  bob@dylan:~$ npm run dev 5-publisher.js
*/

import { createClient } from 'redis';

// Create a Redis publisher client
const publisherClient = createClient();

// Event handler for connection errors
publisherClient.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.toString()}`);
});

// Event handler for successful connection
publisherClient.on('connect', () => {
  console.log('Redis client connected to the server');

  // Function to publish a message after a specified time
  const publishMessage = (message, time) => {
    console.log(`About to send ${message}`);
    setTimeout(() => {
      publisherClient.publish('holberton school channel', message);
    }, time);
  };

  // Publish messages with specified times
  publishMessage('Holberton Student #1 starts course', 100);
  publishMessage('Holberton Student #2 starts course', 200);
  publishMessage('KILL_SERVER', 300);
  publishMessage('Holberton Student #3 starts course', 400);
});
