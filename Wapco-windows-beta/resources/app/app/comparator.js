'use strict'

const path = require('path')
const remote = require('electron').remote
window.remote = remote
let webRoot = path.dirname(__dirname)
window.$ = window.jQuery = require('jquery')
window.controller = require(path.join(webRoot, 'controller.js'))

function get_usernames() {
	var fs = require("fs");
	var exec = require('child_process').exec; 
	var g = document.getElementById("f1").value;
	var h = document.getElementById("f2").value;
	if(!g || !h) {
		alert("Please enter correct value")
		self.location = 'comparator.html'
	}
	else {
		let pyPath = window.controller.getPythonPath()
	  	let pyDir = window.controller.getPythonAppDir()
	  	let script = path.join(pyDir, 'comparator.py')
		var command = pyPath.pythonBin + " " + script + " " + g + " " + h;
		exec(command, function (error, stdout, stderr) {
			if (error !== null) {
		        console.log('exec error: ' + error);
		        return;
		    }
			fs.writeFile('resources/app/app/html/comparator_util.html', stdout,  function(err) {
			   if (err) {
			      console.log(err)
			   }
			})
			self.location = "comparator_util.html"
		});
	}
}