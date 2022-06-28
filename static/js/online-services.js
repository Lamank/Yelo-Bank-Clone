$('input[type=range]').on('input change', function() {
    let range = $(this).val();
    let type = $(this).attr("id");
    let max = parseInt($(this).attr('max')) / 100;
    let percent = parseFloat(range) / max + "%";
    $(this).css('background-size', percent)
    $('input[id=' + type + ']').val(parseFloat(range))

});

$('.range_result').keyup(function() {
    type = $(this).attr("id");
    value = parseFloat($(this).val());
    $('input[id=' + type + ']').val(value);
    max = parseInt($(this).attr('max'));
    percent = parseFloat(value) * 100 / (max) + "%";
    $('input[id=' + type + ']').css('background-size', percent)
    if ($(this).val() > max) {
        $(this).val(max);
        $('input[id=' + type + ']').css('background-size', '100%');
    }
});