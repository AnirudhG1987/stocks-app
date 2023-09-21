from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from . import forms
from django.shortcuts import render
from . import margincalculator
from django.http import JsonResponse
import numpy as np
from datetime import date
# Create your views here.

def index(request):
    form=forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)
    return render(request,'margin_app/index.html',{'form':form})


@csrf_exempt
def myajaxtestview(request):
    excel_data=[]
    if request.method == 'POST':
        liv_script = request.POST['liv_script']
        int_script = request.POST['int_script']
        inv_script = request.POST['inv_script']
        borrowing = int(request.POST['borrowing'])
        living = int(request.POST['living'])
        shares = int(request.POST['shares'])
        stock = int(request.POST['stock'])
        margin_shares = int(request.POST['margin_shares'])
        yearly_living, interest_paid, interest_margin_paid, total_borrowing, total_borrowing_margin, \
            curr_investment, investment_no_margin, investment_margin, stock_price= \
            margincalculator.margin_calculator(inv_script,int_script,liv_script,shares,stock, living,borrowing,margin_shares)

        curr_year = date.today().year
        year = [curr_year+i for i in range(len(yearly_living))]
        age = [curr_year-1987+i for i in range(len(yearly_living))]
        excel_data = [[age[i],year[i],"{0:,.2f}".format(curr_investment[i]),
                       "{0:,.2f}".format(total_borrowing_margin[i]),
                       "{0:,.2f}".format(total_borrowing[i]),
                       "{0:,.2f}".format(yearly_living[i]),
                       "{0:,.2f}".format(interest_paid[i]),
                       "{0:,.2f}".format(interest_paid[i]*3.673),
                       "{0:,.2f}".format(stock_price[i])] for i in range(len(stock_price)-1)]
        excel_data.insert(0, ["Age","Year","Investment","Borrowing Margin","Borrowing","Living"+"{0:,.2f}".format(np.sum(living)),
                              "Interest"+"{0:,.2f}".format(np.sum(interest_paid)),
                              "Interest AED"+"{0:,.2f}".format(np.sum(interest_paid)*3.673),
                              "Stock Price",
                        c    ])


        chart_data_list = [[str(year[i])+'-01',round(curr_investment[i],2),
                            round(investment_no_margin[i],2),round(investment_margin[i],2),
                            round(total_borrowing_margin[i],2),round(total_borrowing[i],2)]
                           for i in range(len(yearly_living)-1)]
        chart_data_list.insert(0, ["Year","NW Current","NW No Margin","NW Margin","Borrowing Margin","Borrowing"])
        interest_data_list = [[str(year[i])+'-01',round(yearly_living[i],2),round(interest_paid[i],2),round(interest_margin_paid[i],2)]
                              for i in range(len(interest_paid))]
        interest_data_list.insert(0, ["Year", "Living","Interest","Interest Margin"])

    return JsonResponse({
            'excel_data': excel_data,
            'xval': year,
            'chart_data' : chart_data_list,
            'interest_data':interest_data_list
    })

