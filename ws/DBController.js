var mongoose = require('mongoose');
var HomePage = require('./homePage.js');
var fs = require('fs');
var mongojs = require('mongojs');

var db1 = mongojs('db_usr:db_pass@ds149278.mlab.com:49278/lab16', ['homePage']);
var db2 = mongojs('db_usr:db_pass@ds149278.mlab.com:49278/lab16', ['artistProfile']);

exports.setData = function(req,res){
    console.log("inside setData");


    var obj;
    var jsonFile = {"data" : obj }

    fs.readFile('data/data1.json', 'utf8', function (err, data) {
          if (err) throw err;
          obj = JSON.parse(data);
      
          var jsonFile = {"data" : obj }

            db1.homePage.insert(jsonFile, function(err, doc) {
                console.log(data);
                if(err) throw err;
            }); 

    });

    fs.readFile('data/data2.json', 'utf8', function (err, data) {
          if (err) throw err;
          obj = JSON.parse(data);
      
          var jsonFile = {"data" : obj }

            db2.artistProfile.insert(jsonFile, function(err, doc) {
                console.log(data);
                if(err) throw err;
                
            }); 

    });


    res.json({"status" : "ok"});
    
    return;

}