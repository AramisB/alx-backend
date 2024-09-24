import express from "express";
import redis from "redis";
import { promisify } from "util";

const listProducts = [
    {
        id: 1,
        name: "Suitcase 250",
        price: 50,
        stock: 4
    },
    {
        id: 2,
        name: "Suitcase 450",
        price: 100,
        stock: 10
    },
    {
        id: 3,
        name: "Suitcase 650",
        price: 350,
        stock: 2
    },
    {
        id: 4,
        name: "Suitcase 1050",
        price: 550,
        stock: 5
    }
];

function getItemById(id) {
    return listProducts.find((item) => item.id === id);
}

const app = express();
app.listen(1245, () => {
    console.log("Server listening on port 1245");
});

app.get("/list_products", (req, res) => {
    res.send(listProducts);
});

const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

function reserveStockById(itemId, stock) {
    client.set(`item.${itemId}`, stock);
}

async function getCurrentReservedStockById(itemId) {
    const reservedStock = await getAsync(`item.${itemId}`);
    return reservedStock;
}

app.get("/list_products/:itemId", async (req, res) => {
    const itemId = Number(req.params.itemId);
    const product = getItemById(itemId);
    
    if (!product) {
        res.status(404).send({
            "status" : "Product not found"
        });
    }
    const reservedStock = await getCurrentReservedStockById(itemId);

    res.send({
        product,
        reservedStock : reservedStock ? parseInt(reservedStock, 10) : 0
    });
});

app.get("/reserve_product/:itemId", async (req, res) => {
    const itemId = Number(req.params.itemId);
    const product = getItemById(itemId);
    
    if (!product) {
        res.status(404).send({
            "status" : "Product not found"
        });
    }
    const reservedStock = await getCurrentReservedStockById(itemId);
    const availableStock = product.stock - (reservedStock ? parseInt(reservedStock, 10) : 0);
    if (availableStock < 1) {
        return res.send({
            "status": "Not enough stock available",
            "itemId": itemId
        });
    } else {
        reserveStockById(itemId, (reservedStock ? parseInt(reservedStock, 10) : 0) + 1);
        return res.send({
            "status": "Reservation confirmed",
            "itemId": itemId
        });
    }
});