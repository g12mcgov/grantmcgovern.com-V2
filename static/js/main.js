/*
* Name: Grant McGovern 
* Date: 25 Jun 2015
*
* main.js
*/

$(document).ready(function() {

    // Particle ground background
    var pg;
	
    start_background();
    start_typist();
    add_card_flips();

    function start_background() {
        $('#particles').particleground({
            dotColor: '#FFFFFF',
            lineColor: '#FFFFFF'
        });
        pg = particleground(document.getElementById('particles'));
    }

    function start_typist() {
        $(function($) {
            $('.typist').typist({
                speed: 13,
                text: 'Grant McGovern'
            });
        });
    };

    // Binds a card flip action to each image
    // under the "My Projects" section.
    function add_card_flips() {
        $('.projects .row .col-md-4').each(function(i, obj) {
            var child = $(obj).children();
            $(child).flip({
                axis: 'x',
                trigger: 'hover'
            });
        });
    };

    $('#terminal').hover(function() {
        pg.pause();
        $('#particles').css('background-color', 'rgba(0, 0, 0, 0.70)'); 
    }, function() {
        $('#particles').css('background-color', 'rgba(0, 0, 0, 0.85)');
        pg.start();
    });
});