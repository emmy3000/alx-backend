#!/usr/bin/node
/*
  Script: 6-job_creator.js

  Description:
  This script uses the Kue library to create a job queue named 'push_notification_code'
  and generates a job with predefined data. It logs relevant messages based on the job's status.

  Requirements:
  - Install dependencies: npm install kue redis
  - Ensure a Redis server is running for Kue storage.

  How to run:
  bob@dylan:~$ npm run dev 6-job_creator.js
*/

import kue from 'kue';

// Create a Kue queue named push_notification_code
const queue = kue.createQueue();

// Object containing the Job data
const jobData = {
  phoneNumber: '1234567890',
  message: 'Hello, this is a notification!',
};

// Create a job with the specified data
const job = queue.create('push_notification_code', jobData);

// Event handler for successful job creation
job.on('complete', () => {
  console.log('Notification job completed');
});

// Event handler for failed job
job.on('failed', () => {
  console.log('Notification job failed');
});

// Save the job to the queue
job.save((err) => {
  if (!err) {
    console.log(`Notification job created: ${job.id}`);
  }
});

// Start the Kue UI
kue.app.listen(3000);
console.log('Kue UI started on port 3000');
