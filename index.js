var express = require('express');
var bodyParser = require('body-parser');
var request = require('request');
var app = express();

app.use(bodyParser.urlencoded({extended: false}));
app.use(bodyParser.json());
app.listen((3000));

app.use(express.static('public'));

// Server frontpage
app.get('/', function (req, res) {
    res.send('This is TestBot Servicjkls');
});

app.get('/schedule/activity/:activity', function(req, res) {
    var result = [{activity:req.params.activity, startTime: "8:00 AM", endTime: "12:00 PM", date: "2016/09/23"},
                {activity:req.params.activity, startTime: "8:00 AM", endTime: "12:00 PM", date: "2016/09/25"}];
    res.send(result);
});
