var express = require('express');
var app = express();
var DBController = require('./DBController');
var DAOontroller = require('./DAOController');



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

//call one time for add json to DB
app.get('/mlab16/insertTODB',DBController.setData);
//get json to homePage
app.get('/mlab16/getHomePage',DAOontroller.getHomePage);
//get json to artistProfile
app.get('/mlab16/getArtistProfile',DAOontroller.getArtistProfile);


app.listen(port);
console.log("service is listeing on port: " + port);