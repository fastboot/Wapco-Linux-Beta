'use strict'

const path = require('path')
const remote = require('electron').remote
window.remote = remote
let webRoot = path.dirname(__dirname)
window.$ = window.jQuery = require('jquery')
window.controller = require(path.join(webRoot, 'controller.js'))

function __chk1() {
	var exec = require('child_process').exec; 
	var g5 = "friends"
	var g6 = document.getElementById("nm3").value;
	var g7 = document.getElementById("ap3").value;
	var g8 = document.getElementById("sc3").value;
	var g9 = document.getElementById("no3").value;
	var g10 = parseInt(g9);
	if(g10 > 50 || !g6 || !g7 || !g8 || !g9) {
		alert("Please fill the fields with correct value")
		self.location = 'analysis3.html'
	}
	else {
		let pyPath = window.controller.getPythonPath()
  		let pyDir = window.controller.getPythonAppDir()
  		let script = path.join(pyDir, 'analysis.py')
		var command = pyPath.pythonBin + " " + script + " " + g5 + " " + g6 + " " + g7 + " " + g8 + " " + g9;
		exec(command, function (error, stdout, stderr) {
			if (error !== null) {
		        console.log('exec error: ' + error);
		        return;
		    }
		    document.write(stdout)
		});
	}
}