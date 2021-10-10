from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from options.optionsdata import *
from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request,'options/index.html',{})


@csrf_exempt
def expiryview(request):
    error_message = ''
    if request.method == 'POST':
        tickers = request.POST['ticker']
        rate_of_rerturn = int(request.POST['rate'])/100
        excel_data_df = get_options_dataframe(tickers,rate_of_rerturn)
        if len(excel_data_df) == 0:
            return JsonResponse({
                'error_message': "No Data. Check Ticker date range"
            })

    excel_data_list = excel_data_df.values.tolist()
    excel_data_list.insert(0,list(excel_data_df.columns))
    chart_data_df = get_ror_strike_per_expiry_df(excel_data_df)
    chart_data_list = chart_data_df.values.tolist()
    chart_data_list.insert(0, list(chart_data_df.columns))
    print(excel_data_df)
    #print(chart_data_list)
    return JsonResponse({
        'error_message': error_message,
        'chart_data': chart_data_list,
        'excel_data': excel_data_list,
    })


@csrf_exempt
def spotview(request):
    error_message = ''
    if request.method == 'POST':
        ticker = request.POST['ticker']
        expiry = request.POST['expiry']
        rate = int(request.POST['rate']) / 100
        chart_data_df = get_ror_strike_per_spot_df(ticker,expiry,rate)
        if len(chart_data_df) == 0:
            return JsonResponse({
                'error_message': "No Data. Check Ticker date range"
            })

    chart_data_list = chart_data_df.values.tolist()
    chart_data_list.insert(0, list(chart_data_df.columns))

    return JsonResponse({
        'error_message': error_message,
        'chart_data': chart_data_list,
        #'excel_data': excel_data_list,
    })

@csrf_exempt
def strikeview(request):
    error_message = ''
    if request.method == 'POST':
        ticker = request.POST['ticker']
        strike = int(request.POST['strike'])
        rate = int(request.POST['rate'])/100
        chart_data_df = get_ror_spot_per_expiry_df(ticker,strike,rate)
        if len(chart_data_df) == 0:
            return JsonResponse({
                'error_message': "No Data. Check Ticker date range"
            })

    chart_data_list = chart_data_df.values.tolist()
    chart_data_list.insert(0, list(chart_data_df.columns))
    print(chart_data_list)
    return JsonResponse({
        'error_message': error_message,
        'chart_data': chart_data_list,
        #'excel_data': excel_data_list,
    })

# Create your views here.
