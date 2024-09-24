import { createClient as redis } from "redis";
import { promisify } from "util";

const client = redis();
const getAsync = promisify(client.get).bind(client);

client.on("error", (error) => {
    console.log("Redis client not connected to the server: " + error);
});

client.on("connect", () => {
    console.log("Redis client connected to the server");
});

client.connect()

function setNewSchool(schoolName, value){
    client.set(schoolName, value, redis.print);    
}

async function displaySchoolValue(schoolName){
    const result = await client.get(schoolName);
    console.log(result);
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
