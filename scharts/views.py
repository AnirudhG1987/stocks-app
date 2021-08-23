from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from scharts.stocksdata import *

# Create your views here.

def index(request):
    return render(request,'charts/index.html',{})


@csrf_exempt
def chartview(request):
    error_message = ''
    if request.method == 'POST':
        tickers = request.POST['ticker'].split(',')
        amount = int(request.POST['amount'])
        freq = int(request.POST['freq'])
        start_year = request.POST['start_period']
        end_year = request.POST['end_period']
        excel_data_df = getstockportfoliodata(amount,tickers,start_year,end_year,freq)
        if len(excel_data_df) == 0:
            return JsonResponse({
                'error_message': "No Data. Check Ticker date range"
            })


    excel_data_list = excel_data_df.values.tolist()
    excel_data_list.insert(0,list(excel_data_df.columns))
    chart_column_list = ['Dates','Investment']
    chart_column_list.extend([stock+" Portfolio" for stock in tickers])#.append('Investment'))
    # put a check box for dividends.
    #chart_column_list.extend([stock + " Portfolio ND" for stock in tickers])
    chart_data_df = excel_data_df[chart_column_list]
    chart_data_list = chart_data_df.values.tolist()
    chart_data_list.insert(0, list(chart_data_df.columns))
    #print(chart_data_list)
    return JsonResponse({
        'error_message': error_message,
        'chart_data': chart_data_list,
        'excel_data': excel_data_list,
    })

