$('#ci_submit').on('click',function() {
   // Recognize what column was chosen
  var shares = document.getElementById('id_share').value;
  var stock = document.getElementById('id_stock').value;
  var borrowing = document.getElementById('id_borrowing').value;
  var living = document.getElementById('id_living').value;
  var int_script = document.getElementById('id_int_script').value;
  var inv_script = document.getElementById('id_inv_script').value;
  var liv_script = document.getElementById('id_liv_script').value;
  var margin_shares = document.getElementById('id_margin_share').value;
  //var row = $(this).closest("tr").index();
  //$('.board').find('tr').eq(row).find('td').eq(col).find('button').text(row);
    //user_id=$('#user_id').text();
  $.ajax({
        type: "POST",
        url: 'my-ajax-test/',
        data: {shares:shares,stock:stock,borrowing:borrowing,living:living,
            int_script:int_script,liv_script:liv_script,inv_script:inv_script,margin_shares:margin_shares}, /* Passing the text data */
        dataType: 'json' ,
        success:  function(response){

                function display() {

                      //-----------------------------------------------------
                      //src w3schools

                       var myEle = document.getElementById("firstTabOverall");
                        if(myEle){
                            myEle.parentNode.removeChild(myEle);
                        }
                      var x = document.createElement('table');
                      x.setAttribute("id","firstTabOverall");

                      x.setAttribute("border", "1");
                      document.body.appendChild(x);

                      //-------------------------------------------------------

                      // //split up display to output each item in array in its own box
                      //     // https://stackoverflow.com/questions/9329446/for-each-over-an-array-in-javascript
                      var index, len;

                       // Create an empty <thead> element and add it to the table:
                        var header = x.createTHead();

                        // Create an empty <tr> element and add it to the first position of <thead>:
                        var row = x.insertRow(0);

                        // Insert a new cell (<td>) at the first position of the "new" <tr> element:
                        for (col=0, col_len = response.excel_data[0].length; col<col_len; ++col){

                            var cell = row.insertCell(col);
                            cell.innerHTML = response.excel_data[0][col];

                        }
                        // Add some bold text in the new cell:



                      for (row = 1, len = response.excel_data.length; row < len; ++row) {
                        var y = document.createElement("TR");
                        y.setAttribute("id", "myTr");
                        document.getElementById("firstTabOverall").appendChild(y);
                        for (col=0, col_len = response.excel_data[row].length; col<col_len; ++col){
                            var t = document.createElement("TD");
                            t.appendChild(document.createTextNode(response.excel_data[row][col]));
                            y.appendChild(t);
                        }
                      }


                }


                function chart(chartName,title,data){
                    //$('#myChart').remove(); // this is my <canvas> element
                    //$('#graph-container').append('<canvas id="myChart"><canvas>');
                    //canvas = document.getElementById('myChart');
                    //var ctx = document.getElementById('myChart').getContext('2d');
                    //var ctx = canvas.getContext('2d');
                    var dataPointsList = [];
                    var chart = new CanvasJS.Chart(chartName, {
                            animationEnabled: true,
                            title:{
                                text: title
                            },
                            axisX:{
                                valueFormatString: "0000",
                                title: "Year",
                                crosshair: {
                                    enabled: true,
                                    snapToDataPoint: true
                                }
                            },
                            axisY: {
                                lineColor: "#C24642",
                                tickColor: "#C24642",
                                labelFontColor: "#C24642",
                                titleFontColor: "#C24642",
                                includeZero: true,
                                title: title,
                                valueFormatString: "$#,##0.00",
                                crosshair: {
                                    enabled: true,
                                    snapToDataPoint: true,
                                    labelFormatter: function(e) {
                                        return "$" + CanvasJS.formatNumber(e.value, "#,##0.00");
                                    }
                                }
                            },

                            legend: {
                                    cursor: "pointer",
                                    itemclick: toggleDataSeries
                                },
                            data: [{
                                xValueFormatString: "0000",
                                yValueFormatString: "$#,##0.00",
                                type: "line",
                                color: "#369EAD",
                                showInLegend: true,
                                dataPoints: dataPointsList
                            }]

                        });

                        function toggleDataSeries(e) {
                            if (typeof (e.dataSeries.visible) === "undefined" || e.dataSeries.visible) {
                                e.dataSeries.visible = false;
                            } else {
                                e.dataSeries.visible = true;
                            }
                            e.chart.render();
                        }
                        function addData(xval,data) {

                            for (var i = 0; i < data.length; i++) {
                                dataPointsList.push({
                                    x: xval[i],
                                    y: data[i]
                                });

                            }

                            chart.render();

                        }


                        addData(response.xval,data);


                    }

                    //chart("chartContainer","Money",response.netw_living,response.netw_noliving);
                    // chart("livchartContainer","Living",response.living);
                    portfoliochart("chartContainer","Net Worth",response.chart_data);
                    portfoliochart("livchartContainer","Living",response.interest_data);
                    display();

                }

});


});

