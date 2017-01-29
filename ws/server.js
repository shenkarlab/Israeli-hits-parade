var express = require('express');
var app = express();
var DAOontroller = require('./DAOController');
var DAController = require('./DBContoller.js');


var port = process.env.PORT || 3000;

app.set('port',port);
app.use('/',express.static('./public'));
app.use(function(req,res,next){
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    app.set('json spaces',4);
    res.set("Content-Type", "application/json");
    next();
});

//insert json files to db
app.get('/mlab16/insert',DAController.setData);
//get details for homePage
app.get('/mlab16/getHomePageDetails',DAOontroller.getHomePageDetails);
//
app.get('/lab16/getHomePageDetails',DAOontroller.getHomePageDetails);

app.listen(port);
console.log("service is listeing on port: " + port);