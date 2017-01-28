var mongoose = require('mongoose');
var HomePage = require('./homePage.js');
var ArtistProfile = require('./artistProfile.js');

exports.getHomePage = function(req,res){
    console.log("inside getHomePage");
    //var userEmail = req.params.email;

    HomePage.find({}).select().
    exec(function(err,result){
       console.log(result);
       res.json(result);
    });

}

exports.getArtistProfile = function(req,res){
    console.log("inside getArtistProfile");

    console.log("inside getHomePage");
    //var userEmail = req.params.email;

    ArtistProfile.find({}).select().
    exec(function(err,result){
       console.log(result);
       res.json(result);
    });

}
