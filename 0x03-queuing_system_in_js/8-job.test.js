import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', () => {
  let queue;

  /**
   * Set up the queue before running tests.
   * Create a new Kue queue and enter test mode without processing jobs.
   */
  before(() => {
    queue = kue.createQueue();
    queue.testMode.enter();
  });

  /**
   * Clear the queue and exit test mode after running tests.
   */
  after(() => {
    queue.testMode.clear();
    queue.testMode.exit();
  });

  /**
   * Test case: display an error message if jobs is not an array.
   */
  it('should display an error message if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs('invalid', queue)).to.throw('Jobs is not an array');
  });

  /**
   * Test case: create two new jobs to the queue.
   */
  it('should create two new jobs to the queue', () => {
    // Sample list of jobs
    const jobsList = [
      { phoneNumber: '4153518780', message: 'This is the code 1234 to verify your account' },
      { phoneNumber: '4153518781', message: 'This is another code to verify your account' },
    ];

    // Call the function to create jobs
    createPushNotificationsJobs(jobsList, queue);

    // Check the number of jobs in the queue
    expect(queue.testMode.jobs.length).to.equal(2);

    // Verify the content of the first job
    const firstJob = queue.testMode.jobs[0];
    expect(firstJob.type).to.equal('push_notification_code_3');
    expect(firstJob.data).to.deep.equal(jobsList[0]);

    // Verify the content of the second job
    const secondJob = queue.testMode.jobs[1];
    expect(secondJob.type).to.equal('push_notification_code_3');
    expect(secondJob.data).to.deep.equal(jobsList[1]);
  });
});
