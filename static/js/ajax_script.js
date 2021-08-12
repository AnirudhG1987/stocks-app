
$('#chart_submit').on('click',function() {
   // Recognize what column was chosen

    var ticker = document.getElementById('id_ticker').value;
    var amount = document.getElementById('id_amount').value;
    var freq = document.getElementById('sip').value;
    var start_period = document.getElementById('start_period').value;
    var end_period = document.getElementById('end_period').value;

  $.ajax({
        type: "POST",
        url: 'chart_ajax/',
        data: {ticker:ticker,amount:amount,freq:freq, start_period:start_period, end_period:end_period}, /* Passing the text data */
        dataType: 'json' ,
        success:  function(response){

                if (response.error_message==""){
                    portfoliochart("sipChart",response.chart_data);
                    display(response.excel_data);
                }
                else{
                    alert(response.error_message);
                }
        }
  });

});
