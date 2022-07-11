var MongoClient = require("mongodb").MongoClient;
var url =
  "mongoserverurl";
us = "jadithyan";
pass="teeemp";
MongoClient.connect(url, function (err, db) {
  if (err) throw err;
  var dbo = db.db("users");
  var query = { username: us };
  dbo
    .collection("users")
    .find(query)
    .toArray(function (err, result) {
      if (err) throw err;
      pass = result[0].password;
      console.log(pass);
      console.log(result);
      db.close();
    });
})