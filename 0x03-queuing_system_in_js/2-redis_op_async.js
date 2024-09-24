import { createClient as redis } from "redis";
import { promisify } from "util";

const client = redis();
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

client.on("error", (error) => {
    console.log("Redis client not connected to the server: " + error);
});

client.on("connect", () => {
    console.log("Redis client connected to the server");
});

async function connectToRedis() {
    try {
        await client.connect();
    } catch (error) {
        console.error("Could not connect to Redis:", error);
    }
}

async function setNewSchool(schoolName, value) {
    try {
        await setAsync(schoolName, value);
    } catch (error) {
        console.error("Error setting school value: ", error);
    }
}

async function displaySchoolValue(schoolName) {
    try {
        const result = await getAsync(schoolName);
        console.log(result);
    } catch (error) {
        console.error("Error getting school value: ", error);
    }
}

async function run() {
    await connectToRedis();
    await displaySchoolValue('Holberton');
    await setNewSchool('HolbertonSanFrancisco', '100');
    await displaySchoolValue('HolbertonSanFrancisco');
}

run();
