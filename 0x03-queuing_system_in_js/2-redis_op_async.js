#!/usr/bin/node
/*
  Script: 2-redis_op_async.js

  Description:
  This script utilizes the 'redis' package to establish a connection with a Redis server.
  It builds upon the functionality of the previous script (1-redis_op.js)
  by introducing two additional functions: setNewSchool and displaySchoolValue.
  
  - setNewSchool: Takes two arguments, schoolName and value,
    and sets the provided value for the specified key (schoolName) in Redis.
  
  - displaySchoolValue: A function modified to leverage ES6 async/await.
    It retrieves and displays the value associated with a given schoolName from the Redis server.

  The script demonstrates asynchronous operations using async/await
  and promisify from the 'util' module, enhancing readability and control flow.
*/

import { promisify } from "util";
import { createClient, print } from "redis";

// Create a Redis client
const client = createClient();

// Event handler for connection errors
client.on("error", (err) => {
  console.log("Redis client not connected to the server:", err.toString());
});

// Function to set a new school value in Redis
const setNewSchool = (schoolName, value) => {
  return new Promise((resolve, reject) => {
    client.set(schoolName, value, (err, reply) => {
      if (err) {
        reject(err);
      } else {
        print(`Reply: ${reply}`);
        resolve(reply);
      }
    });
  });
};

// Function to display the value for a given school in Redis
const displaySchoolValue = async (schoolName) => {
  // Use promisify to convert the callback-based client.get into a promise-based function
  return await promisify(client.get).bind(client)(schoolName);
};

// Main function to execute operations
async function main() {
  // Display the value for the key 'Holberton'
  console.log(await displaySchoolValue("Holberton"));

  // Set a new school value for the key 'HolbertonSanFrancisco'
  try {
    await setNewSchool("HolbertonSanFrancisco", "100");
  } catch (error) {
    console.error("Error setting new school value:", error);
  }

  // Introducing a slight delay
  await new Promise((resolve) => setTimeout(resolve, 500));

  // Display the updated value for the key 'HolbertonSanFrancisco'
  console.log(await displaySchoolValue("HolbertonSanFrancisco"));
}

// Event handler for successful connection
client.on("connect", async () => {
  // Log a message when the Redis client is connected to the server
  console.log("Redis client connected to the server");

  // Execute the main function to perform Redis operations
  await main();
});
