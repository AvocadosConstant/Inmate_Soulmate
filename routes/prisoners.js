exports.findById = function(req, res) {
    var MongoClient = require('mongodb').MongoClient;
    MongoClient.connect("mongodb://localhost/test", function(err, db) {
	if(err) { return console.dir(err); }
	var collection = db.collection('prisoners');
	collection.findOne({'_id' : req.params.id}, function(err, item) {
	    res.send(item);
	});
    });
};