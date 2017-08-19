
$(document).ready(function() {
    $("#professionalism").hide();
    $("#brotherhood").hide();
    $("#schools").hide();
    $("#employers-more").hide();
    $("#campus").hide();

    $("#btn-professionalism").click(function() {
        $("#brotherhood").hide();
        $("#philanthropy").hide();
        $("#professionalism").slideDown();
    });

    $("#btn-philanthropy").click(function() {
        $("#brotherhood").hide();
        $("#professionalism").hide();
        $("#philanthropy").slideDown();
    });

    $("#btn-brotherhood").click(function() {
        $("#philanthropy").hide();
        $("#professionalism").hide();
        $("#brotherhood").slideDown();
    });

    $("#btn-employers").click(function() {
        $("#schools").hide();
        $("#campus").hide();
        $("#employers-more").hide();
        $("#btn-see-more").show();
        $("#employers").slideDown();
    });

    $("#btn-schools").click(function() {
        $("#employers").hide();
        $("#campus").hide();
        $("#employers-more").hide();
        $("#btn-see-more").show();
        $("#schools").slideDown();
    });

    $("#btn-campus").click(function() {
        $("#employers").hide();
        $("#schools").hide();
        $("#employers-more").hide();
        $("#btn-see-more").show();
        $("#campus").slideDown();
    });

    $("#btn-see-more").click(function() {
        $("#employers-more").slideDown();
        $("#btn-see-more").hide();
        $("#btn-see-less").show();
    });

    $("#btn-see-less").click(function() {
        $("#employers-more").slideUp();
        $("#btn-see-more").show();
        $("#btn-see-less").hide();
    });


    $(".nav-home").click(function() {
        $('html, body').animate({
            scrollTop: $("#home").offset().top
        }, 1000);
    });

    $(".nav-apply").click(function() {
        $('html, body').animate({
            scrollTop: $("#apply").offset().top
        }, 1000);
    });

    $(".nav-about-us").click(function() {
        $('html, body').animate({
            scrollTop: $("#about-us").offset().top
        }, 1000);
    });

    $(".nav-portfolio").click(function() {
        $('html, body').animate({
            scrollTop: $("#portfolio").offset().top
        }, 1000);
    });

    $(".nav-brothers").click(function() {
        $('html, body').animate({
            scrollTop: $("#brothers").offset().top
        }, 1000);
    });

    $(".nav-contact").click(function() {
        $('html, body').animate({
            scrollTop: $("#contact").offset().top
        }, 1000);
    });

    // Animate the scroll to top
    $('.go-top').click(function(event) {
        event.preventDefault();

        $('html, body').animate({scrollTop: 0}, 300);
    })


});