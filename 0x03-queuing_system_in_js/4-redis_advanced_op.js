// Using hset, let’s store the following:

// The key of the hash should be HolbertonSchools
// It should have a value for:
// Portland=50
// Seattle=80
// New York=20
// Bogota=20
// Cali=40
// Paris=2
// Make sure you use redis.print for each hset
// Display Hash:
// Using hgetall, display the object stored in Redis. It should return the following:

// Requirements:

// Use callbacks for any of the operation, we will look at async operations later

import redis from "redis";

const client = redis.createClient();

client.hset("HolbertonSchools", "Portland", "50", redis.print);
client.hset("HolbertonSchools", "Seattle", "80", redis.print);
client.hset("HolbertonSchools", "New York", "20", redis.print);
client.hset("HolbertonSchools", "Bogota", "20", redis.print);
client.hset("HolbertonSchools", "Cali", "40", redis.print);
client.hset("HolbertonSchools", "Paris", "2", redis.print);

client.hgetall("HolbertonSchools", (err, value) => {
    console.log(value);
    client.quit();
});
