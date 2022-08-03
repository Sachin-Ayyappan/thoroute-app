var express = require("express");
var bodyParser = require("body-parser");

const mongoose = require("mongoose");
mongoose.connect(
  "mongodb+srv://thoroute-app:thoroute%402022adi@thoroute.vd7gshc.mongodb.net/users"
);
var db = mongoose.connection;
db.on("error", console.log.bind(console, "connection error"));
db.once("open", function (callback) {
  console.log("connection succeeded");
});
var app = express();

app.use(bodyParser.json());
app.use(express.static("public"));
app.use(
  bodyParser.urlencoded({
    extended: true,
  })
);

app.post("/sign_up", function (req, res) {
  var fname = req.body.firstname;
  var lname = req.body.lastname;
  var uname = req.body.username;
  var email = req.body.email;
  var pass = req.body.password;
  var phone = req.body.number;

  var data = {
    firstname: fname,
    lastname: lname,
    username: uname,
    email: email,
    password: pass,
    phone: phone,
  };
  db.collection("users").insertOne(data, function (err, collection) {
    if (err) throw err;
    console.log("Record inserted Successfully");
  });
  return res.redirect("http://localhost:5500/assets/dashboard/pages/samples/login.html");
});

app
  .get("/", function (req, res) {
    res.set({
      "Access-control-Allow-Origin": "*",
    });
    return res.redirect("index.html");
  })
  .listen(3001);

console.log("User registration server listening at port 3001");
