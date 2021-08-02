
$('#chart_submit').on('click',function() {
   // Recognize what column was chosen

    var ticker = document.getElementById('id_ticker').value;
    var amount = document.getElementById('id_amount').value;
    var freq = document.getElementById('sip').value;
    var period = document.getElementById('period').value;

  $.ajax({
        type: "POST",
        url: 'chart_ajax/',
        data: {ticker:ticker,amount:amount,freq:freq, period:period}, /* Passing the text data */
        dataType: 'json' ,
        success:  function(response){
                //stockchart("shareChart",ticker,response.dates_data ,response.stock_data);
                portfoliochart("sipChart","Investment",response.dates_data,response.investment,response.portfolio,response.stock_data, response.stock_return);
                //portfoliochart("shareChart","Investment",response.dates_data,response.investment,response.portfolio);
                //portfoliochart("sipChart","Investment",response.dates,response.investment,response.portfolio);

                display(response.excel_data);
        }
  });

});
