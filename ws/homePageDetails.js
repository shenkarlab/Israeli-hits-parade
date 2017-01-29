var mongoose = require('mongoose');
var schema = mongoose.Schema;

var testPageSchema = new schema({
    year: { type:String, index:1 },
	songs : [{ position: String,
			 commonWordInLyrics: String,
			 gender: String, 
			 lyricsHtml : String,
			 songName: String,
			 artist: String,
			 category : [String] ,
			 lyricsText : String ,
			 lyricsUrl : String ,
			 wordsAmount : Number }]
}, {collection:'songs'} );

var song = mongoose.model('song',testPageSchema);
module.exports = song;



