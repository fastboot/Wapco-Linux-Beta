'use strict'

const path = require('path')
const remote = require('electron').remote
window.remote = remote
let webRoot = path.dirname(__dirname)
window.$ = window.jQuery = require('jquery')
window.controller = require(path.join(webRoot, 'controller.js'))

function chk() {
	var exec = require('child_process').exec; 
	var g2 = document.getElementById("nm1").value;
	var h2 = document.getElementById("nm2").value;
	var h4 = document.getElementById("no3").value;
	var h5 = parseInt(h4)
	if(h5 > 50 || !g2 || !h2) {
		alert("Please fill the fields with correct value")
		self.location = 'analysis2.html'	
	}
	else {
		var g3 = "1"
		let pyPath = window.controller.getPythonPath()
  		let pyDir = window.controller.getPythonAppDir()
  		let script = path.join(pyDir, 'analysis.py')
		var command = pyPath.pythonBin + " " + script + " " + g3 + " " + g2 + " " + h2 + " " + h4;
		exec(command, function (error, stdout, stderr) {
			if (error !== null) {
		        console.log('exec error: ' + error);
		        return;
		    }
		    document.write(stdout)
		});
	}
}