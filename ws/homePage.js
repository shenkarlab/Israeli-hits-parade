var mongoose = require('mongoose');
var schema = mongoose.Schema;

var homePageSchema = new schema({
    data : [{songs : [{ position: String, mostCommomWord: String, gender: String, songName: String, artist: String, category : [String] }], year: { type:String, index:1 } }]
}, {collection:'homePage'} );

var HomePage = mongoose.model('HomePage',homePageSchema);
module.exports = HomePage;



