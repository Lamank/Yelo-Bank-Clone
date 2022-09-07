let hamburger_menu = $("#hamburger");


hamburger_menu.on("click", function (event) {
    $("#bars").toggleClass("fa-bars");
    $("#bars").toggleClass("fa-xmark");
    $(".bttm_nav_links, .head_extra, .main, footer, .extra").toggleClass("display_none");
    $('.head_extra').css('transition', "all 0.2s");
    $(".head_extra , .extra").removeClass("display_block");

});


window.addEventListener('scroll', function (event) {
    if (this.scrollY >= 15) {
        $('#header_top').hide();
        $('.header_bottom').css({ 'background-color': 'white', 'border-bottom': '1px solid #ECECEC' });
        $('.internet_button').css({ 'width': '50px', 'border-radius': '50%', 'padding': '10px 16.8px' })
    
    }

    else {
        $('#header_top').show();
        $('.header_bottom').css({ 'background-color': 'transparent', 'border-bottom': 'none' });
        $('.internet_button').css({ 'width': '170px', 'border-radius': '30px' })
    }
});


$('#searching').on('click', function () {
    $(".search").show()
    $('#header_top ,.header_bottom').hide()
    $('html, body').css({
        overflow: 'hidden',
        height: '100%'
    });
    $('.main').css('opacity', '0.8')
});

$('.fa-xmark').on('click', function () {
    $(".search").hide()
    $('.header_top, .header_bottom').show()
    $('html, body').css({
        overflow: 'auto',
        height: 'auto'
    });
    $('.main').css('opacity', '1')
});