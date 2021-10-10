
$('#expiry_submit').on('click',function() {
   // Recognize what column was chosen

    var ticker = document.getElementById('id_ticker').value;
    var rate = document.getElementById('id_rate').value;

  $.ajax({
        type: "POST",
        url: 'expiry_ajax/',
        data: {ticker:ticker,rate:rate}, /* Passing the text data */
        dataType: 'json' ,
        success:  function(response){
                console.log("successful expiry")
                if (response.error_message==""){
                    optionchart("expiryChart","Expiry Comparison",response.chart_data);
                    //display(response.excel_data);
                }
                else{
                    alert(response.error_message);
                }
        }
  });

});


$('#strike_submit').on('click',function() {
   // Recognize what column was chosen

    var ticker = document.getElementById('id_ticker').value;
    var strike = document.getElementById('id_strike').value;
    var rate = document.getElementById('id_rate').value;

  $.ajax({
        type: "POST",
        url: 'strike_ajax/',
        data: {ticker:ticker,strike:strike,rate:rate}, /* Passing the text data */
        dataType: 'json' ,
        success:  function(response){
                console.log("successful strike")
                if (response.error_message==""){
                    optionchart("strikeChart","Strike Comparison",response.chart_data);
                    //display(response.excel_data);
                }
                else{
                    alert(response.error_message);
                }
        }
  });

});


$('#spot_submit').on('click',function() {
   // Recognize what column was chosen

    var ticker = document.getElementById('id_ticker').value;
    var expiry = document.getElementById('id_expiry').value;
    var rate = document.getElementById('id_rate').value;

  $.ajax({
        type: "POST",
        url: 'spot_ajax/',
        data: {ticker:ticker,expiry:expiry,rate:rate}, /* Passing the text data */
        //dataType: 'json' ,
        success:  function(response){
                if (response.error_message==""){
                    console.log(response.chart_data);
                    optionchart("spotChart","Spot Comparison",response.chart_data);
                    display(response.excel_data);
                }
                else{
                    alert(response.error_message);
                }
        }
  });

});


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
                    portfoliochart("sipChart","Stock Comparison",response.chart_data);
                    display(response.excel_data);
                }
                else{
                    alert(response.error_message);
                }
        }
  });

});
