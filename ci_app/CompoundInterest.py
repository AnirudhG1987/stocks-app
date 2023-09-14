import numpy as np
def calculator(ci_script,ci_living,amount):
    #print("i am inside")
    #print(ci_living)
    ci_list = ci_script.split(';')
    ci_living_list = ci_living.split(';')

    principal_noliving = []
    principal_living = []
    living = []
    principal_living.append(amount)
    principal_noliving.append(amount)
    living.append(0)
    #print(ci_living_list)
    growth_rate_array = np.empty(0)
    expense_rate_array = np.empty(0)

    for ci_tenor in ci_list:
        tenor = int(ci_tenor.split(',')[0])
        rate = float(ci_tenor.split(',')[1])
        growth_rate_array = np.append(growth_rate_array,np.full(tenor,rate))

    #print(growth_rate_array)

    for living_tenor in ci_living_list:
        tenor = int(living_tenor.split(',')[0])
        living_rate = float(living_tenor.split(',')[1])
        expense_rate_array = np.append(expense_rate_array, np.full(tenor, living_rate))
    #print(expense_rate_array)

    for i in range(max(len(expense_rate_array),len(growth_rate_array))):
        if i < len(growth_rate_array) and i < len(expense_rate_array):
            principal_noliving.append(principal_noliving[-1] * (1 + growth_rate_array[i] / 100))
            principal_living.append(principal_living[-1] * (1 + growth_rate_array[i] / 100)*(1 - expense_rate_array[i] / 100) )
            living.append(principal_living[-1] * expense_rate_array[i] / (100 - expense_rate_array[i]))

        if i >= len(growth_rate_array):
            principal_noliving.append(principal_noliving[-1])
            principal_living.append(principal_living[-1] * (1 - expense_rate_array[i] / 100) )
            living.append(principal_living[-1] * expense_rate_array[i] / 100)

        if i >= len(expense_rate_array):
            principal_noliving.append(principal_noliving[-1] * (1 + growth_rate_array[i] / 100))
            principal_living.append(principal_living[-1] * (1 + growth_rate_array[i] / 100) - living[-1] )
            living.append(living[-1])

    return principal_noliving, principal_living,living

#x, y, z = calculator("5,50","2,2;5,4",1000)
#print(x)
#print(y)
#print(z)