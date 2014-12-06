var Browser = require("zombie");
var assert = require("assert");

browser = new Browser()
browser.visit("http://www.dcor.state.ga.us:80/GDC/OffenderQuery/jsp/OffQryForm.jsp", function() {
    console.log(browser.html());
    browser.pressButton("submit2", function() {
	assert.ok(browser.success);
	console.log(browser.html());
    })
});
