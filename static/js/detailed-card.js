$(document).ready(function() {
    $('.slick').slick({
        slidesToShow: 3,
        slidesToScroll: 1,

        focusOnSelect: true,
    });
});

function Colorize() {
    let colors = ['#0091FE', '#947EEC', '#FF3A33', '#0FDB9D', '#75842F', '#2174C3', '#F799B9', '#55CD62', '#A523E6'];
    let color = colors[Math.floor(Math.random() * colors.length)];
    return color
};
let feature_sign = $(".feature_sign");


for (let i = 0; i <= feature_sign.length; i++) {
    let color = Colorize();
    feature_sign[i].style.backgroundColor = color;
}