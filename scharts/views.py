from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from scharts.stocksdata import *
import numpy as np
import pandas as pd

# Create your views here.

def index(request):
    return render(request,'charts/index.html',{})


@csrf_exempt
def chartview(request):
    stock_data=[]
    no_of_shares = []
    investment = []
    excel_data = []
    failure_msg = ''
    if request.method == 'POST':
        tickers = request.POST['ticker'].split(',')
        amount = int(request.POST['amount'])
        freq = int(request.POST['freq'])
        start_year = request.POST['start_period']
        end_year = request.POST['end_period']
        stock_data, error_message = getstockdatarange(tickers,start_year,end_year,freq)
        portfolio = []
        if stock_data.empty:
            return JsonResponse({
                'error_message': error_message
            })


        dates_data = np.datetime_as_string(stock_data.index.values, unit='D')
        investment.append(amount)
        no_of_shares.append(round(amount / stock_data[0],2))
        portfolio.append(round(no_of_shares[-1] * stock_data[0],2))
        for i in range(1,len(stock_data)):
            investment.append(amount + investment[-1])
            no_of_shares.append(round(amount / stock_data[i] + no_of_shares[-1], 2))
            portfolio.append(round(no_of_shares[-1] * stock_data[i],2))

        excel_data = [[dates_data[i], "{0:,.2f}".format(stock_data[i]), "{0:,.2f}".format(investment[i]),
                        no_of_shares[i], "{0:,.2f}".format(portfolio[i])] for i in range(len(investment))]
        excel_data.insert(0, ["Dates", "Share Price",  "Investment","Shares", "Networth"])
        #stock_return = cagr(float(amount),float(portfolio[-1]),int(period))
        #print(stock_return)
    return JsonResponse({
        'error_message': error_message,
        'stock_data': stock_data.values.round().tolist(),
        'dates_data': dates_data.tolist(),
        'investment': investment,
        'portfolio': portfolio,
        'excel_data': excel_data,
    })

