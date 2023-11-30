#!/usr/bin/node
/*
  Script: 7-job_creator.js

  Description:
  This script uses the Kue library to create a job queue named 'push_notification_code_2'.
  It initializes an array of jobs and creates individual jobs for each object in the array.
  The script logs relevant messages based on the job's status, such as job creation, completion,
  failure, and progress.

  Requirements:
  - Install dependencies: npm install kue redis
  - Ensure a Redis server is running for Kue storage.

  How to run:
  bob@dylan:~$ npm run dev 7-job_creator.js
*/

import kue from 'kue';

// Create an array of jobs
const jobs = [
  { phoneNumber: '4153518780', message: 'This is the code 1234 to verify your account' },
  { phoneNumber: '4153518781', message: 'This is the code 4562 to verify your account' },
  { phoneNumber: '4153518743', message: 'This is the code 4321 to verify your account' },
  { phoneNumber: '4153538781', message: 'This is the code 4562 to verify your account' },
  { phoneNumber: '4153118782', message: 'This is the code 4321 to verify your account' },
  { phoneNumber: '4153718781', message: 'This is the code 4562 to verify your account' },
  { phoneNumber: '4159518782', message: 'This is the code 4321 to verify your account' },
  { phoneNumber: '4158718781', message: 'This is the code 4562 to verify your account' },
  { phoneNumber: '4153818782', message: 'This is the code 4321 to verify your account' },
  { phoneNumber: '4154318781', message: 'This is the code 4562 to verify your account' },
  { phoneNumber: '4151218782', message: 'This is the code 4321 to verify your account' },
];

// Create a Kue queue named push_notification_code_2
const queue = kue.createQueue();

// Loop through the array of jobs
jobs.forEach((jobData, index) => {
  // Create a new job for each object in the array
  const job = queue.create('push_notification_code_2', jobData);

  // Event handler for successful job creation
  job.on('complete', () => {
    console.log(`Notification job ${job.id} completed`);
  });

  // Event handler for failed job
  job.on('failed', (errorMessage) => {
    console.log(`Notification job ${job.id} failed: ${errorMessage}`);
  });

  // Event handler for job progress
  job.on('progress', (progress) => {
    console.log(`Notification job ${job.id} ${progress}% complete`);
  });

  // Save the job to the queue
  job.save((err) => {
    if (!err) {
      console.log(`Notification job created: ${job.id}`);
    }
  });
});

// Start the Kue UI
kue.app.listen(3000);
console.log('Kue UI started on port 3000');
