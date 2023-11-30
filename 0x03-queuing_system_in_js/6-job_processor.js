#!/usr/bin/node
/*
  Script: 6-job_processor.js

  Description:
  This script uses Kue to process jobs from the 'push_notification_code' queue.
  It defines a function 'sendNotification' and sets up a queue process to execute it for new jobs.

  Requirements:
  - Install dependencies: npm install kue redis
  - Ensure a Redis server is running for Kue storage.

  How to run:
  Terminal 2: bob@dylan:~$ npm run dev 6-job_processor.js
  Terminal 1: bob@dylan:~$ npm run dev 6-job_creator.js
*/

import kue from "kue";

// Create a Kue queue named push_notification_code
const queue = kue.createQueue();

// Function to send a notification
const sendNotification = (phoneNumber, message) => {
  console.log(
    `Sending notification to ${phoneNumber}, with message: ${message}`
  );
};

// Process jobs from the push_notification_code queue
queue.process("push_notification_code", (job, done) => {
  // Call the sendNotification function with job data
  sendNotification(job.data.phoneNumber, job.data.message);
  // Mark the job as completed
  done();
});

// Output message when the processor is ready
console.log("Job processor is ready");
