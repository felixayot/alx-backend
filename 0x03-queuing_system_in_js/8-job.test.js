// Tests createPushNotificationsJobs function and the queue object.

const createPushNotificationsJobs = require("./8-job");
const kue = require("kue");
const chai = require("chai");

const queue = kue.createQueue();

const list = [
  {
    phoneNumber: "4153518780",
    message: "This is the code 1234 to verify your account",
  },
  {
    phoneNumber: "4153518781",
    message: "This is the code 1235 to verify your account",
  },
];

describe("createPushNotificationsJobs", () => {
  beforeEach(() => {
    queue.testMode.enter();
  });

  afterEach(() => {
    queue.testMode.clear();
  });

  after(() => {
    queue.testMode.exit();
  });

  it("display an error message if jobs is not an array", () => {
    chai
      .expect(() => createPushNotificationsJobs("jobs", queue))
      .to.throw("Jobs is not an array");
  });

  it("display an error message if jobs is not a Number array", () => {
    chai
      .expect(() => {
        createPushNotificationsJobs(2, queue);
      })
      .to.throw("Jobs is not an array");
  });

  it("display an error message if jobs is not an array Object", () => {
    chai
      .expect(() => {
        createPushNotificationsJobs({}, queue);
      })
      .to.throw("Jobs is not an array");
  });

  it("display an error message if jobs is not an array string", () => {
    chai
      .expect(() => {
        createPushNotificationsJobs("Holberton", queue);
      })
      .to.throw("Jobs is not an array");
  });

  it("should NOT display an error message if jobs is an array with empty array", () => {
    const ret = createPushNotificationsJobs([], queue);
    chai.expect(ret).to.equal(undefined);
  });

  it("create two new jobs to the queue", () => {
    createPushNotificationsJobs(list, queue);
    chai.expect(queue.testMode.list.length).to.equal(2);
    chai
      .expect(queue.testMode.list[0].type)
      .to.equal("push_notification_code_3");
    chai.expect(queue.testMode.list[0].data).to.eql({
      phoneNumber: "4153518780",
      message: "This is the code 1234 to verify your account",
    });
    chai
      .expect(queue.testMode.list[1].type)
      .to.equal("push_notification_code_3");
    chai.expect(queue.testMode.list[1].data).to.eql({
      phoneNumber: "4153518781",
      message: "This is the code 1235 to verify your account",
    });
  });
});
