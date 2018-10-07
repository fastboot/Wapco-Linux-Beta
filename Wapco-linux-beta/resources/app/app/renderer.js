'use strict'

const path = require('path')
const remote = require('electron').remote
window.remote = remote
window.$ = window.jQuery = require('jquery')
let webRoot = path.dirname(__dirname)
window.controller = require(path.join(webRoot, 'controller.js'))

$('window').ready(function () {
  if (window.controller.getPythonPath() === null) {
    let options = {
      title: 'Python?',
      type: 'info',
      message: 'Python version 3+ not found.\nPlease install it.',
      buttons: []
    }
    remote.dialog.showMessageBox(window.remote.getCurrentWindow(), options)
  }
  else {
    window.controller.initPythonWin32(window.controller.getPythonDepends())
  }
})


