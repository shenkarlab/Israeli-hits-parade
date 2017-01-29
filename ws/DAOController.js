var mongoose = require('mongoose');
var song = require('./homePageDetails.js');

mongoose.Promise = global.Promise; 

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


exports.getHomePageDetails = function(req,res){
    console.log("inside getHomePageDetails");
    //var userEmail = req.params.email;
    song.find({}).sort('year').
    exec(function(err,result){
       console.log(result);
       res.json(result);
    });

}