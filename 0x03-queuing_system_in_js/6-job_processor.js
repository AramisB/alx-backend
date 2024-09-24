import kue from "kue";
// Create a queue with Kue
const queue = kue.createQueue();
// Create a function named sendNotification:
// It will take two arguments phoneNumber and message
// It will log to the console Sending notification to PHONE_NUMBER, with message: MESSAGE
// Write the queue process that will listen to new jobs on push_notification_code:
function sendNotification(phoneNumber, message) {
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}
// Every new job should call the sendNotification function with the phone number and the message contained within the job data
queue.process("push_notification_code", 2, (job, done) => {
    sendNotification(job.data.phoneNumber, job.data.message);
    done();
})
