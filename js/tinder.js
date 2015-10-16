function nextPrisoner() {
    $.get("/prisoners/1000773329", function(data) {
	$("#infobox").html(function() {
	    return data['name'] + "<br>Height: " + data['height']
		+ "<br>Weight: " + data['weight'] + " lbs"
		+ "<br>Age: " + ((new Date().getFullYear()) - data['birthyear']);
	});
	$("#prisonerpic").attr("src", "http://www.dcor.state.ga.us/images/offenders/" + data['_id'] + ".jpg");
    });
}

nextPrisoner();