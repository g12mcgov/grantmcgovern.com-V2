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

    // Hide the 'Highcharts.com' text
    $('text:contains("Highcharts.com")').css('display', 'none');

    function start_background() {
        $('#particles').particleground({
            dotColor: '#FFFFFF',
            lineColor: '#FFFFFF'
        });
        pg = particleground(document.getElementById('particles'));
        add_waypoint();
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

    var terminal_hover_text = $(
        '<span class="terminal-hover-text">'
        +   'Check out my plugin, '
        +   '<a href="https://github.com/g12mcgov/Terminal.js">'
        +       'Terminal.js'
        +   '</a>'
        +'</span>'
        );

    $('#terminal').hover(function() {
        pg.pause();
        $('.typist').typistStop();
        $('#particles').css('background-color', 'rgba(0, 0, 0, 0.70)'); 
        
        terminal_hover_text.hide();
        terminal_hover_text.insertAfter('#terminal');
        terminal_hover_text.fadeIn(1500);
    
    }, function() {
        $('#particles').css('background-color', 'rgba(0, 0, 0, 0.85)');
        terminal_hover_text.fadeOut(1500);

        pg.start();
    });

    /* Setup waypoints */
    function add_waypoint() {
        var typist_lock = false;
        var waypoint = new Waypoint({
            element: document.getElementById('middle-intro-text'),
            handler: function() {
                if(!typist_lock) {
                    $(this.element).typist({
                        speed: 9,
                        text: "Hi, I'm Grant."
                    });
                    typist_lock = true;
                }
            },
            offset: '50%'
        });
    };

    $('#about-popover').on('click', function(e) {e.preventDefault(); return true;});
    $("[data-toggle=popover]").popover({html:true});
    // $('#dropdown-arrow').click(function() {
    //     $(this).toggle(function(){
    //         console.log('opened');
    //         //$(this).toggleClass("glyphicon glyphicon-chevron-down");
    //     }, function() {
    //         console.log('closed');
    //         $(this).toggleClass("glyphicon glyphicon-chevron-up");
    //     });
    // });
});