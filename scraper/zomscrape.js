var Browser = require("zombie");
var assert = require("assert");
var MongoClient = require('mongodb').MongoClient;
var jf = require('jsonfile');
var searchUrl = "http://www.dcor.state.ga.us:80/GDC/OffenderQuery/jsp/OffQryForm.jsp"
/*
function addPrisoner(html) {
    return false;  
}
*/
MongoClient.connect("mongodb://localhost:27017/prisoners", function(err, db) {
    if(!err) {
	console.log("We are connected");
    }
});

browser = new Browser()
browser.visit(searchUrl, function() {
    //console.log(browser.html());
    browser.pressButton("submit2", function() {
	assert.ok(browser.success);
	jf.readFile('prisonlist.json', function(err, obj) {
	    for(var p in obj) {
		browser.visit(searchUrl, function() {
		    browser.select("vCurrentInstitution", obj[p], function() {
			browser.pressButton("NextButton", function() {
			    addPrisoner(browser.html());
			});
		    });
		});
	    }
	});
    });
}