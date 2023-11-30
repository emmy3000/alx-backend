#!/usr/bin/node
/*
  Script: 5-subscriber.js

  Description:
  This script creates a Redis subscriber client that connects to a Redis server.
  It subscribes to the channel "holberton school channel" and logs received messages.
  If the message received is "KILL_SERVER," it unsubscribes and quits.

  Requirements:
  - Use the 'redis' package.
  - Run with Node.js.

  How to run:
  bob@dylan:~$ npm run dev 5-subscriber.js
*/

import { createClient } from 'redis';

// Create a Redis subscriber client
const subscriberClient = createClient();

// Event handler for connection errors
subscriberClient.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.toString()}`);
});

// Event handler for successful connection
subscriberClient.on('connect', () => {
  console.log('Redis client connected to the server');

  // Subscribe to the "holberton school channel"
  subscriberClient.subscribe('holberton school channel');

  // Event handler for received messages
  subscriberClient.on('message', (channel, message) => {
    console.log(message);

    // Unsubscribe and quit if message is "KILL_SERVER"
    if (message === 'KILL_SERVER') {
      subscriberClient.unsubscribe();
      subscriberClient.quit();
    }
  });
});
