const connectToMongo = require("./db");
const cors = require("cors");
const express = require("express");
const bodyParser = require("body-parser");
const app = express();
const port = process.env.PORT || 3000;

connectToMongo();

app.use(express.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
app.use(cors());

app.use("/api/missingpeople", require("./routes/missing"));
app.use("/api/foundlocation", require("./routes/location"));

// Start the server with error handling
app
  .listen(port, () => {
    console.log(`Example app listening at http://localhost:${port}`);
  })
  .on("error", (err) => {
    if (err.code === "EADDRINUSE") {
      console.error(`Port ${port} is already in use.`);
    } else {
      console.error(`Error starting server: ${err}`);
    }
  });
