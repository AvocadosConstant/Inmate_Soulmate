var http = require('http');

var options = {
    host: 'www.dcor.state.ga.us',
    port: 80,
    path: '/GDC/OffenderQuery/jsp/OffQryRedirector.jsp',
    method: 'POST',
    headers: {
	'Content-Type' : 'application/x-www-form-urlencoded',
	'Cookie' : ''
    }
};

var data = JSON.stringify( {
    "vIsCookieEnabled" : "Y",
    "vUnoCaseNoRadioButton" : "none",
    "vLastName" : "+",
    "vGender" : "MALE",
    "vRace" : "ASIAN",
    "vScope" : "ACTIVE",
    "RecordsPerPage" : "150",
    "NextPage" : "2",
    "vDetailFormat" : "Summary",
} );

var req = http.request(options, function(res) {
    console.log('STATUS: ' + res.statusCode);
    console.log('HEADERS: ' + JSON.stringify(res.headers));
    res.setEncoding('utf8');
    res.on('data', function (chunk) {
	console.log('BODY: ' + chunk);
    });
});

req.on('error', function(e) {
    console.log('problem with request: ' + e.message);
});

// write data to request body
req.write(data);
req.end();