// Express server for stock data in redis client queue

const express = require("express");
const redis = require("redis");
const promisify = require("util").promisify;

// Stock Data

const listProducts = [
  {
    itemId: 1,
    itemName: "Suitcase 250",
    price: 50,
    initialAvailableQuantity: 4,
  },
  {
    itemId: 2,
    itemName: "Suitcase 450",
    price: 100,
    initialAvailableQuantity: 10,
  },
  {
    itemId: 3,
    itemName: "Suitcase 650",
    price: 350,
    initialAvailableQuantity: 2,
  },
  {
    itemId: 4,
    itemName: "Suitcase 1050",
    price: 550,
    initialAvailableQuantity: 5,
  },
];

function getItemById(itemId) {
  return listProducts.find((item) => item.itemId === itemId);
}

// Redis client

const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);

client.on("error", (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

client.on("connect", () => {
  console.log("Redis client connected to the server");
});

function reserveStockById(itemId, stock) {
  client.set(`item.${itemId}`, stock);
}

async function getCurrentReservedStockById(itemId) {
  const stock = await getAsync(`item.${itemId}`);
  return stock;
}

// Express server

const app = express();
const port = 1245;
const notFound = { status: "Product not found" };

app.listen(port, () => {
  console.log(`app running at http://localhost:${port}`);
});

app.get("/list_products", (req, res) => {
  res.json(listProducts);
});

app.get("/list_products/:itemId", async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const item = getItemById(itemId);
  if (item) {
    res.json(item);
  } else {
    res.json(notFound);
    return;
  }

  const currentStock = await getCurrentReservedStockById(itemId);
  const stock = currentStock ? currentStock : item.initialAvailableQuantity;
  item.currentQuantity = stock;
  res.json(item);
});

app.get("/reserve_product/:itemId", async (req, res) => {
  const itemId = Number(req.params.itemId);
  const item = getItemById(itemId);
  const noStock = { status: "Not enough stock available", itemId };
  const reservationConfirmed = { status: "Reservation confirmed", itemId };

  if (!item) {
    res.json(notFound);
    return;
  }

  let currentStock = await getCurrentReservedStockById(itemId);
  if (currentStock === null) currentStock = item.initialAvailableQuantity;

  if (currentStock <= 0) {
    res.json(noStock);
    return;
  }

  reserveStockById(itemId, Number(currentStock) - 1);
  res.json(reservationConfirmed);
});
