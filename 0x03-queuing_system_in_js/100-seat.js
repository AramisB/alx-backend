import redis from "redis";
import { promisify } from "util";
import kue from "kue";
import express from "express";

const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

function reserveSeat(number) {
    setAsync("available_seats", number);
}

function getCurrentAvailableSeats() {
    return getAsync("available_seats");
}

// Initialize with 50 seats
reserveSeat(50);
setAsync("reservationEnabled", true);

const queue = kue.createQueue();

const app = express();
app.listen(1245, () => {
    console.log("Server listening on port 1245");
});

// Endpoint to get available seats
app.get("/available_seats", async (req, res) => {
    const availableSeats = await getCurrentAvailableSeats();
    res.send({
        numberOfAvailableSeats: parseInt(availableSeats, 10)
    });
});

// Endpoint to reserve a seat
app.get("/reserve_seat", async (req, res) => {
    const reservationEnabled = await getAsync("reservationEnabled"); // Fetch from Redis

    if (reservationEnabled !== "true") {
        return res.send({
            status: "Reservations are blocked"
        });
    }

    const job = queue.create("reserve_seat").save((error) => {
        if (!error) {
            console.log("Seat reservation job" + job.id + " completed");
        } else {
            console.log("Seat reservation job" + job.id + " failed: ", error);
        }
    });

    job.on("complete", () => {
        console.log("Seat reservation job " + job.id + " completed");
    }).on("failed", (error) => {
        console.log("Seat reservation job " + job.id + " failed: ", error);
    });

    res.send({
        status: "Reservation in process"
    });
});

// Endpoint to process reservations
app.get("/process", async (req, res) => {
    res.send({ status: "Queue processing" });

    const availableSeats = await getCurrentAvailableSeats();
    const newAvailableSeats = parseInt(availableSeats, 10) - 1;

    if (newAvailableSeats < 0) {
        throw new Error("Not enough seats available");
    }

    reserveSeat(newAvailableSeats);

    if (newAvailableSeats === 0) {
        await setAsync("reservationEnabled", false);
    }
});
