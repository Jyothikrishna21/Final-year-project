const mongoose = require("mongoose");
const mongoURI = "mongodb://localhost:27017/Face_Recognition";

const connectToMongo = () => {
  mongoose.set("strictQuery", true);
  mongoose
    .connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log("Connected to Mongo successfully"))
    .catch((err) => console.error("Failed to connect to MongoDB", err));
};

module.exports = connectToMongo;
