
let cr_item_buy = $('.cr_item_buy');
let cr_item_sell = $('.cr_item_sell');
let cr_list = [];
for (let i = 0; i < cr_item_buy.length; i++) {
  cr_list.push(parseFloat(cr_item_buy[i].innerText));
  cr_item_buy[i].innerText = cr_list[i].toFixed(4);

  if (i == 0) {
    cr_item_sell[i].innerText = (cr_list[i] + 0.002).toFixed(4);
  }
  else {
    cr_item_sell[i].innerText = (cr_list[i] + 0.11).toFixed(4);
  }
} $('.input_value').keyup(function () {
  exchange_calculator();
  this.value = this.value.replace(/[^0-9.]/g, '').replace(/(\..*?)\..*/g, '$1');
});

let exchange_calculator = () => {
  let input_result = $('#input_result');


  $('#from option').each(function () {
    if (this.selected) {
      cur_value = this.value;
      return cur_value;
    }
  });
  $('#to option').each(function () {
    if (this.selected) {
      to_value = this.value;
      return to_value;
    }
  });
  let sell = document.querySelector('[name="sell"]').value;
  let value = 0

  if (cur_value == 'azn' && sell != '') {
    if (to_value === 'usd') {
      value = parseFloat(sell) / parseFloat(cr_item_sell[0].innerText);
    }
    else {
      value = parseFloat(sell) / parseFloat(cr_item_sell[1].innerText);
    }

    input_result.text(value.toFixed(2));


  }

  else if (cur_value == 'usd' && sell != '') {

     value = parseFloat(sell) * parseFloat(cr_item_buy[0].innerText);
    input_result.text(value.toFixed(2));

  }
  else if (cur_value == 'eur' && sell != '') {

    value = parseFloat(sell) * parseFloat(cr_item_buy[1].innerText);
    input_result.text(value.toFixed(2));
  }
  else if (sell === '') {

    input_result.text('Alıram');
  }
}

let selected_value = () => {
  $('#from option').each(function () {
    if (this.selected) {
      cur_value = this.value

      if (cur_value == 'usd' || cur_value == 'eur') {
        $("#azn").css("display", "block");
        $("#usd").css("display", "none");
        $("#eur").css("display", "none");
        $("#usd").removeAttr('selected');
        $("#azn").prop("selected", true);

      }

      else if (cur_value == 'azn') {
        $("#azn").css("display", "none");
        $("#usd").css("display", "block");
        $("#eur").css("display", "block");
        $("#azn").removeAttr('selected');
        $("#usd").prop("selected", true);

      }
      exchange_calculator();

    }
  });

}


let loan_calculate = (period, amount) => {


  if ($('input[name=month]').val() != '' && $('input[name=credit]').val() != '' && $('input[name=month]').val() != 0 && $('input[name=credit]').val() != 0) {
    let i = 20 / 12 / 100;
    let in_r = Math.pow(1 + i, period);

    let month_amount = (amount * (i * in_r) / (in_r - 1));
    let month_amount_list = month_amount.toFixed(2).split('.');
    $('#month_pay').html(month_amount_list[0] + `.<span style="font-size:10px;" >` + month_amount_list[1] + `</span>
  <span>AZN</span>`);
    return month_amount
  }

}

let limit_credit = (m_amount) => {
  let salary = parseFloat($('input[name=salary]').val()) * 45 / 100;
  let amount = parseFloat($('input[name=credit]').val());
  
  if (m_amount >= salary) {
    // console.log(salary);

    amount = parseInt(amount*0.7);
    console.log(amount);
    $('input[name=month], input[id=month]').val(48);
    $('input[name=credit], input[id=credit]').val(amount)
    $('input[id=month]').css('background-size', '100%')
    let percent = amount * 100 / 30000 + "%"
    $('input[id=credit]').css('background-size', percent)
  }
}


$('input[type=range]').on('input change', function () {
  let range = $(this).val();
  let type = $(this).attr("id");
  let max = parseInt($(this).attr('max')) / 100;
  let percent = parseFloat(range) / max + "%";
  $(this).css('background-size', percent)
  $('input[name=' + type + ']').val(parseFloat(range))
  let period = parseFloat($('input[name=month]').val());
  let amount = parseFloat($('input[name=credit]').val());

  m_amount = loan_calculate(period, amount);
  // console.log(m_amount);


  limit_credit(m_amount);
  // loan_calculate(period, amount)
});


$('.range_result').keyup(function () {

  type = $(this).attr("name");
  value = parseFloat($(this).val());
  $('input[id=' + type + ']').val(value);

  max = parseInt($(this).attr('max'));
  // console.log("range_result "+max);
  percent = parseFloat(value) * 100 / (max) + "%";
  // console.log(percent);
  $('input[id=' + type + ']').css('background-size', percent)

  if ($(this).val() > max) {
    $(this).val(max);
    $('input[id=' + type + ']').css('background-size', '100%');
    // console.log($(this).val());
  }
  this.value = this.value.replace(/[^0-9.]/g, '').replace(/(\..*?)\..*/g, '$1');
  let period = parseFloat($('input[name=month]').val());
  let amount = parseFloat($('input[name=credit]').val());

  m_amount = loan_calculate(period, amount);

  limit_credit(m_amount);
  // loan_calculate(period, amount)
});




