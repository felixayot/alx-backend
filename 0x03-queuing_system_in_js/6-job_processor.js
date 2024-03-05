// Creates a queue and processes the jobs

const kue = require('kue');
const queue = kue.createQueue();

// Logs a 'Sending notification ...' to the console
function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

queue.process('push_notification_code', (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message);
  done();
}
);
