// Creates a job with Kue and adds it to the queue

const kue = require("kue");
const queue = kue.createQueue();

const jobData = {
  phoneNumber: "0763000000",
  message: "This is One Equity Number!",
};

const job = queue.create("push_notification_code", jobData).save((err) => {
  if (!err) console.log(`Notification job created: ${job.id}`);
  else console.log(err);
});

job.on("complete", () => console.log("Notification job completed"));
job.on("failed", () => console.log("Notification job failed"));
