/*
*	Terminal.js
*	
* 	A terminal emulator in your browser... what?!
*
*	Author: Grant McGovern
*	Date: 17 June 2015
*/

document.addEventListener('DOMContentLoaded', function() {

	// Grab the main terminal div
	var terminal = document.getElementById('terminal');

	// Cache to hold commands
	var cache = [];

	// Root text 
	var root = 'grantmcgovern@gMAC-2:~/<span style="color:#FF00FF;">Developer</span> $ ';

	// Input form 
	var input;

	// List of commands and their actions
	// ~ Stored in `command` => `action` (key/val) format
	var commands = {
		ls: function() { 
			displayText('/about<br>');
			displayText('/home<br>');
			displayText('/github<br>');
		},
		ll: function() {
			displayText('.<br>');
			displayText('..<br>');
			displayText('.bash_profile<br>');
			displayText('.bash_history<br>');
			displayText('<span style="color:blue;">about</span><br>');
			displayText('<span style="color:blue;">home</span><br>');
			displayText('<span style="color:yellow;">github</span><br>');
		}, 
		cd: function(directory) {
			// Check if it was called with no args 
			directory = (typeof directory !== 'undefined') ? directory : null;

			if(!directory) {
				displayText("-bash: cd takes [1] argument <br>");
			}
			else {
				switch (directory[0]) {
					case '/about':
						window.location.href = '/about';
						break;
					case '/github':
						window.location.href = 'http://github.com/g12mcgov';
						break;
					default:
						window.location.href = '/';
						break;
				}
			}
		},
		mailx: function(body) {
			window.location.href = 'mailto:grantmcgovern.mcgovern@gmail.com?body=' + body;
		},
		help: function() {
			displayText('Available commands:<br>');
			displayText('ls -- list directory contents ( [ls] [file ...])<br>');
			displayText('cd -- change directory ( [cd] [directory ...])<br>');
		},
		h: function() {
			displayText('Available commands:<br>');
			displayText('ls -- list directory contents ( [ls] [file ...])<br>');
			displayText('cd -- change directory ( [cd] [directory ...])<br>');
		},
		who: function() {
			displayText("grantmcgovern console  Jun 22 18:52<br>");
		}	
	};

	// Add root text 
	addRootText();

	// Append input_form dynamically to div 
	addInputForm();

	// Move cursor to input prompt
	activateCursor();

	// Listen for enter key press
	document.onkeypress = function(event) {
		if(event.keyCode == 13) {
  			cache.push(input.value);
  			handleCommand(input.value);
  			addRootText();
  			addInputForm();
  			activateCursor();
		}
	};

	// Listen for up-arrow key press
	document.onkeydown = function(event) {
		if(event.keyCode == 38) {
			var last_command = cache[0];
			console.log(last_command);
			//console.log(cache);
		}
	}

	function handleCommand(command) {
		cleanTerminal();
		command_list = command.split(' ');

		if(command_list.length > 1) {
			command = command_list[0];
			args = command_list.slice(1);
			executeCommandArgs(command, args);
		}
		else {
			executeCommandNoArgs(command);
		}
	}

	function addInputForm() {
		input = document.createElement('input');
		input.type = 'text';
		input.id = 'user_input';
		// On page load, set cursor focus to terminal element
		terminal.appendChild(input);
	}

	function addRootText() {
		terminal.innerHTML += '<span>' + root + '</span>';	
	}

	function displayText(text) {
		terminal.innerHTML += '<span>' + text + '</span>';
	}

	function cleanTerminal() {
		terminal.removeChild(input);
		var newline = document.createElement('br');
		terminal.appendChild(newline);
	};

	function activateCursor() {
		input.focus();
		input.select();
	}

	function executeCommandArgs(command, args) {
		if(command in commands) {
			// Perform action
			if(typeof(commands[command]) == 'function') {
				commands[command](args);
			}
		}
		else {
			displayText(
				"-bash: " + command + ": command not found" + "<br>"
				);
		}
	};

	function executeCommandNoArgs(command) {
		if(command in commands) {
			// Perform action
			if(typeof(commands[command]) == 'function') {
				commands[command]();
			}
		}
		else {
			displayText(
				"-bash: " + command + ": command not found" + "<br>"
				);
		}
	};
});