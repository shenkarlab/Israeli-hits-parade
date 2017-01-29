var mongoose = require('mongoose');
var song = require('./homePageDetails.js');
var fs = require('fs');
var mongojs = require('mongojs');

var db1 = mongojs('db_usr:db_pass@ds133249.mlab.com:33249/lab16', ['songs']);
// var db2 = mongojs('db_usr:db_pass@ds149278.mlab.com:49278/lab16', ['artistProfile']);

exports.setData = function(req,res){
    console.log("inside setData");


    var obj;
    // var jsonFile = {"data" : obj }

    for(index = 1 ; index < 8 ; index++ ){

          fs.readFile('data/'+index+'.json', 'utf8', function (err, data) {
          
          if (err) throw err;
          obj = JSON.parse(data);
      
            // var jsonFile = {"data" : obj }
            db1.songs.insert(obj, function(err, doc) {
                console.log(data);
                if(err) throw err;
            }); 

    });
    }


    res.json({"status" : "ok"});
    
    return;

}