import kue from 'kue';

/**
 * Create push notification jobs.
 * @param {Object[]} jobs - Array of job objects.
 * @param {kue.Queue} queue - Kue queue.
 * @throws {Error} If jobs is not an array.
 */
function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  jobs.forEach((jobData) => {
    // Create a new job for each object in the array
    const job = queue.create('push_notification_code_3', jobData);

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
}

export default createPushNotificationsJobs;
