var express = require('express');
var bodyParser = require('body-parser');
var request = require('request');
var app = express();

app.use(bodyParser.urlencoded({extended: false}));
app.use(bodyParser.json());
app.listen((3000));

// Server frontpage
app.get('/', function (req, res) {
    res.send('This is TestBot Server');
});
