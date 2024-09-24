import redis from "redis";
// create a redis client:
const client = redis.createClient();
// On connect, it should log the message Redis client connected to the server
client.on("connect", () => {
    console.log("Redis client connected to the server");
})
// On error, it should log the message Redis client not connected to the server: ERROR MESSAGE
client.on("error", (error) => {
    console.log("Redis client not connected to the server: " + error);
})
// Write a function named publishMessage:
// It will take two arguments: message (string), and time (integer - in ms)
// After time millisecond:
// The function should log to the console About to send MESSAGE
// The function should publish to the channel holberton school channel, the message passed in argument after the time passed in arguments

function publishMessage(message, time) {
    setTimeout(() => {
        console.log("About to send " + message);
        client.publish("holberton school channel", message);
    }, time);
    client.on("message", (channel, message) => {
        if (message === "KILL_SERVER") {
            client.unsubscribe();
            client.quit();
        }
        console.log(message);
    })    
}
// At the end of the file, call:
publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);