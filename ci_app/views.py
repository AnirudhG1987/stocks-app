from django.views.decorators.csrf import csrf_exempt

from . import forms
from django.shortcuts import render
from . import CompoundInterest
from django.http import JsonResponse
import numpy as np
from datetime import date

def index(request):
    form=forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)
    return render(request,'ci_app/index.html',{'form':form})


@csrf_exempt
def myajaxtestview(request):
    excel_data=[]
    if request.method == 'POST':
        ci_script = request.POST['script']
        if request.POST['living'] != '':
            ci_living = int(request.POST['living'])
        else:
            ci_living = 0
        amount = int(request.POST['amount'])
        principal_noliving, principal_living, living = CompoundInterest.calculator(ci_script, ci_living, amount)
        print(living)
        curr_year = date.today().year
        year = [curr_year+i for i in range(len(principal_living))]
        age = [curr_year-1987+i for i in range(len(principal_living))]
        excel_data = [[age[i],year[i],"{0:,.2f}".format(principal_noliving[i]),"{0:,.2f}".format(principal_living[i]),
                       "{0:,.2f}".format(max(principal_living[i]-principal_living[i-1],0)), "{0:,.2f}".format(living[i]),
                                         "{0:,.2f}".format(living[i]*3.673)] for i in range(len(principal_living))]
        excel_data.insert(0, ["Age","Year","Principal","Principal_Living","Increment", "Living "+"{0:,.2f}".format(np.sum(living)),
                              "Living AED "+"{0:,.2f}".format(np.sum(living)*3.673)])

        chart_data_list = [[str(year[i])+'-01',round(principal_noliving[i],2),round(principal_living[i],2)] for i in range(len(principal_living))]
        chart_data_list.insert(0, ["Dates","NetW n Living","NetW Living"])
        living_data_list = [[str(year[i])+'-01',round(living[i],2)] for i in range(len(living))]
        living_data_list.insert(0, ["Dates", "Living"])

    return JsonResponse({
            'excel_data': excel_data,
            'xval': year,
            'chart_data' : chart_data_list,
            'living':living_data_list
    })

