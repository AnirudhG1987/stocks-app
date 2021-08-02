function display(data) {

                var myEle = document.getElementById("firstTabOverall");
                if(myEle){
                    myEle.parentNode.removeChild(myEle);
                }
                var x = document.createElement('table');
                x.setAttribute("id","firstTabOverall");

                x.setAttribute("border", "1");
                document.body.appendChild(x);

                var index, len;
                var header = x.createTHead();
                var row = x.insertRow(0);
                for (col=0, col_len = data[0].length; col<col_len; ++col){

                    var cell = row.insertCell(col);
                    cell.innerHTML = data[0][col];

                }

                for (row = 1, len = data.length; row < len; ++row) {
                    var y = document.createElement("TR");
                    y.setAttribute("id", "myTr");
                    document.getElementById("firstTabOverall").appendChild(y);
                    for (col=0, col_len = data[row].length; col<col_len; ++col){
                        var t = document.createElement("TD");
                        t.appendChild(document.createTextNode(data[row][col]));
                        y.appendChild(t);
                    }
                }
}

function portfoliochart(chartName,title,dates,investment,portfolio,stock_data,stock_return){

        var dataList = []

        var chart = new CanvasJS.StockChart(chartName,{
        title:{
          text:title
        },
        subtitles:[{
            text: Math.round(portfolio[portfolio.length-1]/investment[investment.length-1])+"X"
        },
        {
            text: stock_return+"%"
        }],
        animationEnabled: true,
        rangeSelector: {
            enabled: false
        },
        navigator: {
            enabled: false
        },
        exportEnabled: true,
        charts: [{
          axisX: {
            valueFormatString: "MM YYYY",
            title: "Year",
            crosshair: {
              enabled: true,
              snapToDataPoint: true
            }
          },
          axisY2: {
            prefix: "$",
            title: "stock price",
          },
          axisY: {
            title: title,
            valueFormatString: "$#,##0.00",
            crosshair: {
              enabled: true,
              snapToDataPoint: true,
                labelFormatter: function(e) {
                    return "$" + CanvasJS.formatNumber(e.value, "#,##0.00");
                }
              //snapToDataPoint: true
            }
          },
          data: dataList
        }],

      });



    function addData(xval,data, name, secondary ) {
        var dataSeries = {type: "spline"}
        if (secondary){
            dataSeries.axisYType = "secondary"
        }
        dataSeries.showInLegend =  true
        dataSeries.name = name

        var dataPoints = [];
        for (var i = 0; i < data.length; i++) {
            dataPoints.push({
                x: new Date(xval[i]),
                //x: xval[i],
                y: data[i]
            });
        }
        dataSeries.dataPoints = dataPoints
        dataList.push(dataSeries);
    }

    function toggleDataSeries(e) {
        if (typeof (e.dataSeries.visible) === "undefined" || e.dataSeries.visible) {
            e.dataSeries.visible = false;
        } else {
            e.dataSeries.visible = true;
        }
        e.chart.render();
    }
    addData(dates,investment, "investment",false);
    addData(dates,portfolio,"portfolio",false);
    addData(dates,stock_data,"stock price",true);
    chart.render();


}

function stockchart(chartName,title,dates, data){
        var dps1 = [], dps2= [];
        var dataPointsList = [];
        var stockChart = new CanvasJS.StockChart(chartName,{
        title:{
          text:title
        },
        animationEnabled: true,
        exportEnabled: true,
        charts: [{
          axisX: {
            valueFormatString: "MM YYYY",
            title: "Year",
            crosshair: {
              enabled: true,
              snapToDataPoint: true
            }
          },
          axisY: {
            title: title,
            valueFormatString: "$#,##0.00",

            crosshair: {
              enabled: true,
              snapToDataPoint: true,
                labelFormatter: function(e) {
                    return "$" + CanvasJS.formatNumber(e.value, "#,##0.00");
                }
              //snapToDataPoint: true
            }
          },
          data: dps1
        }],
        navigator: {
          data: [{
            dataPoints: dps2
          }],
          slider: {
            minimum: new Date(2021, 01, 01),
            maximum: new Date(2021, 12, 31)
          }
        }
      });


    function addData(xval,data) {
        var dataSeries = { type: "spline" };
        var dataPoints = [];
        for (var i = 0; i < data.length; i++) {
            dataPoints.push({
                x: new Date(xval[i]),
                //x: xval[i],
                y: data[i]
            });
            dps2.push({
                x: new Date(xval[i]),
                //x: xval[i]
                y: data[i]
            });

        }
        dataSeries.dataPoints = dataPoints;
        dps1.push(dataSeries);
        //console.log(dataPointsList)

    }


    addData(dates,data);
    console.log(dps1);

    stockChart.render();
}



