var express = require('express');
var app = express();
var path = require("path");

app.get('/', function(req, res) {
	res.sendFile(path.join(__dirname+'/index.html'));
});

app.post('/', function(req, res) {
	console.log('test');
	res.send("test");
})

app.listen(3000, function() {
	console.log("Listening on 3000");
});





