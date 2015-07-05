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
                speed: 9,
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
        $('.typist').typistStop();
        $('#particles').css('background-color', 'rgba(0, 0, 0, 0.70)'); 
    }, function() {
        $('#particles').css('background-color', 'rgba(0, 0, 0, 0.85)');
        pg.start();
    });

    /* LinkedIn */
    $.ajax({
        type: 'GET',
        jsonpCallback: "callback",
        dataType: 'jsonp',
        url: 'https://api.linkedin.com/v1/people/~',
        data: {'format': 'jsonp' },
        headers: {'Authorization': 'Bearer AQUuDHPQFjREOyCTDYDQZk86HVtUJzQ2WELeu_7biY0YB6MI4e0HcI-ukocvjombyxB26f-xBA-oIm_L82MR0PiICCsUc-fJXRh15ewQbBw_Y-rNZfOoblL4jYkcecPpL4HTQIxX1igDdQm9ANdyyBAmPFDNuXCrwguh8CWoHWusLMclloI'},
        success: function(reponse) {
            console.log(this.url);
            console.log(reponse);
        },
        error: function(err) {
        }
    });
});