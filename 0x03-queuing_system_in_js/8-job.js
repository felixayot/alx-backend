// Create a job queue that accepts functions and runs them in order.

const createPushNotificationsJobs = (jobs, queue) => {
  if (!Array.isArray(jobs)) throw new Error("Jobs is not an array");

  const jobQueue = "push_notification_code_3";
  jobs.forEach((jobFormat) => {
    const job = queue.create(jobQueue, jobFormat).save((err) => {
      if (!err) console.log(`Notification job created: ${job.id}`);
    });
    job.on("complete", () =>
      console.log(`Notification job ${job.id} completed`)
    );
    job.on("failed", (err) =>
      console.log(`Notification job ${job.id} failed: ${err}`)
    );
    job.on("progress", (progress) =>
      console.log(`Notification job ${job.id} ${progress}% complete`)
    );
  });
};

module.exports = createPushNotificationsJobs;
