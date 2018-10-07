'use strict'

const path = require('path')
const remote = require('electron').remote
window.remote = remote
let webRoot = path.dirname(__dirname)
window.$ = window.jQuery = require('jquery')
window.controller = require(path.join(webRoot, 'controller.js'))

function get_country() {
	var exec = require('child_process').exec; 
	let pyPath = window.controller.getPythonPath()
  	let pyDir = window.controller.getPythonAppDir()
  	let script = path.join(pyDir, 'country.py')
	var command = pyPath.pythonBin + " " + script 
	var output;
	exec(command, function (error, stdout, stderr) {
		if (error !== null) {
	        console.log('exec error: ' + error);
	        return;
	    }
	    output = stdout
	    document.getElementById('rs').innerHTML = `${output}`;
	});
}
function get_city() {
	var exec = require('child_process').exec; 
	let pyPath = window.controller.getPythonPath()
  	let pyDir = window.controller.getPythonAppDir()
  	let script = path.join(pyDir, 'city.py')
	var command = pyPath.pythonBin + " " + script
	var output;
	exec(command, function (error, stdout, stderr) {
		if (error !== null) {
	        console.log('exec error: ' + error);
	        return;
	    }
	    output = stdout
	  	document.getElementById('ct').innerHTML = `${output}`;
	});
}

function get_org() {
	var exec = require('child_process').exec; 
	let pyPath = window.controller.getPythonPath()
  	let pyDir = window.controller.getPythonAppDir()
  	let script = path.join(pyDir, 'ins.py')
	var command = pyPath.pythonBin + " " + script 
	var output;
	exec(command, function (error, stdout, stderr) {
		if (error !== null) {
	        console.log('exec error: ' + error);
	        return;
	    }
	    output = stdout
	   	document.getElementById('ogr').innerHTML = `${output}`;
	});
}

function get_lang() {
	var exec = require('child_process').exec; 
	let pyPath = window.controller.getPythonPath()
  	let pyDir = window.controller.getPythonAppDir()
  	let script = path.join(pyDir, 'language.py')
	var command = pyPath.pythonBin + " " + script 
	var output;
	exec(command, function (error, stdout, stderr) {
		if (error !== null) {
	        console.log('exec error: ' + error);
	        return;
	    }
	    output = stdout
	   	document.getElementById('lng').innerHTML = `${output}`;
	});
}


