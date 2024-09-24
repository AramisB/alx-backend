import kue from "kue";
const blacklisted = ["4153518780", "4153518781"];

function sendNotification(phoneNumber, message, job, done) {
    if (blacklisted.includes(phoneNumber)) {
        return done (new Error("Phone number " + phoneNumber + " is blacklisted"));
    }
    else {
        job.progress(50);
        console.log("Sending notification to " + phoneNumber + ", with message: " + message);
    }
    done();
}

const queue = kue.createQueue();
queue.process("push_notification_code_2", 2, (job, done) => {
    sendNotification(job.data.phoneNumber, job.data.message, job, done);
})