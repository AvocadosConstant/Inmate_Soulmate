var http = require('http');
var express = require('express'), prisoners = require('./routes/prisoners');
var app = express();

app.get('/prisoners/:id', prisoners.findById);

app.listen(3000);
console.log('Now listening on port 3000');