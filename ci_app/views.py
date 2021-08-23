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
        principal, living = CompoundInterest.calculator(ci_script, ci_living, amount)
        curr_year = date.today().year
        year = [curr_year+i for i in range(len(principal))]
        age = [curr_year-1987+i for i in range(len(principal))]
        excel_data = [[age[i],year[i],"{0:,.2f}".format(principal[i]),
                       "{0:,.2f}".format(max(principal[i]-principal[i-1],0)), "{0:,.2f}".format(living[i]),
                                         "{0:,.2f}".format(living[i]*3.673)] for i in range(len(principal))]
        excel_data.insert(0, ["Age","Year","Principal","Increment", "Living "+"{0:,.2f}".format(np.sum(living)),
                              "Living AED "+"{0:,.2f}".format(np.sum(living)*3.673)])



    return JsonResponse({
            'excel_data': excel_data,
            'xval': year,
            'netw': principal,
            'living':living
    })

