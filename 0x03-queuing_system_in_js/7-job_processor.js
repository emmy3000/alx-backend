#!/usr/bin/node
/*
  Script: 7-job_processor.js

  Description:
  This script creates a Kue queue named 'push_notification_code_2' to process jobs
  for sending notifications. It tracks job progress, checks for blacklisted phone
  numbers, and logs relevant messages on success or failure.

  Requirements:
  - Install dependencies: npm install kue redis
  - Ensure a Redis server is running for Kue storage.

  How to run:
  bob@dylan:~$ npm run dev 7-job_processor.js
*/

import kue from 'kue';

// Create an array of blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

// Create a function to send notifications
const sendNotification = (phoneNumber, message, job, done) => {
  // Track the progress of the job
  job.progress(0);

  // Check if the phone number is blacklisted
  if (blacklistedNumbers.includes(phoneNumber)) {
    // Fail the job with an error
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  // Log progress and send the notification
  job.progress(50);
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

  // Complete the job
  done();
};

// Create a Kue queue named push_notification_code_2
const queue = kue.createQueue();

// Process jobs from the push_notification_code_2 queue
queue.process('push_notification_code_2', 2, (job, done) => {
  // Extract data from the job
  const { phoneNumber, message } = job.data;

  // Call the sendNotification function with job data
  sendNotification(phoneNumber, message, job, done);
});

// Output message when the processor is ready
console.log('Job processor is ready');
