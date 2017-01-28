var mongoose = require('mongoose');
var schema = mongoose.Schema;

var artistProfileSchema = new schema({
    data : [ {winAmount: Number,  songs : [{ songName: String, lyrics: String, year: String }], artist: { type:String, index:1 } }]
}, {collection:'artistProfile'} );

var ArtistProfile = mongoose.model('ArtistProfile',artistProfileSchema);
module.exports = ArtistProfile;



