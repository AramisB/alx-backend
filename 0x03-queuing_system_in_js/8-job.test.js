import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';
import { expect } from 'chai';

// Create a queue with Kue
const queue = kue.createQueue();
queue.testMode = true; // Enable test mode

describe("createPushNotificationsJobs", () => {
    it("should throw an error if jobs is not an array", () => {
        const list = {
            phoneNumber: '4153518780',
            message: 'This is the code 1234 to verify your account'
        };
        // Use Chai's expect().to.throw()
        expect(() => createPushNotificationsJobs(list, queue)).to.throw("Jobs is not an array");
    });
    
    it("should create jobs in the queue and log messages", () => {
        const list = [
            {
                phoneNumber: '4153518780',
                message: 'This is the code 1234 to verify your account'
            }
        ];
        const consoleLogSpy = sinon.spy(console, 'log'); // Use Sinon to spy on console.log

        createPushNotificationsJobs(list, queue);

        // Check that jobs are added to the queue
        expect(queue.testMode.jobs).to.have.lengthOf(1); // Expect one job to be created

        // Check that console.log was called for job creation
        expect(consoleLogSpy).to.have.been.calledWithMatch("Notification job created:");

        // Restore the console.log spy
        consoleLogSpy.restore();
    });
});
