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
    if request.method == 'POST':
        ticker = request.POST['ticker']
        amount = int(request.POST['amount'])
        freq = int(request.POST['freq'])
        period = request.POST['period']
        stock_data = getstockdata(ticker,period,freq)

        dates_data = np.datetime_as_string(stock_data.index.values, unit='D')
        share_dates, share_price, dates = [], [], []
        portfolio = []
        # investment.append(0)
        # no_of_shares.append(0)
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
        stock_return = cagr(amount,portfolio[-1],period)
    return JsonResponse({
        'stock_data': stock_data.values.round().tolist(),
        'dates_data': dates_data.tolist(),
        'investment': investment,
        'portfolio': portfolio,
        'excel_data': excel_data,
        'return': stock_return,
    })

