import redis from "redis";

// create a redis client:
const client = redis.createClient();

// On connect, it should log the message Redis client connected to the server
client.on("connect", () => {
    console.log("Redis client connected to the server");
});
// On error, it should log the message Redis client not connected to the server: ERROR MESSAGE
client.on("error", (error) => {
    console.log("Redis client not connected to the server: " + error);
});
// It should subscribe to the channel holberton school channel
client.subscribe("holberton school channel");

// When it receives message on the channel holberton school channel, it should log the message to the console
// When the message is KILL_SERVER, it should unsubscribe and quit
client.on("message", (channel, message) => {
    if (message === "KILL_SERVER") {
        client.unsubscribe();
        client.quit();
    } else {
        console.log(message);
    }
});