import { createClient as redis } from "redis";

const client = redis();

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

function displaySchoolValue(schoolName){
    client.get(schoolName, (error, result) => {
        if (error) {
            console.log(error);
        } else {
            console.log(result);
        }
    });
}

setNewSchool('Holberton', '100');
displaySchoolValue('Holberton');
