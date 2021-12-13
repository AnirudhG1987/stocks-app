
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
    print(ci_living_list)

    for ci_tenor in ci_list:
        tenor = int(ci_tenor.split(',')[0])
        rate = float(ci_tenor.split(',')[1])
        for i in range(tenor):
            principal_noliving.append(principal_noliving[-1] * (1 + rate / 100))
            principal_living.append(principal_living[-1] * (1 + rate / 100))

    multiplier = 1
    index = 1
    for living_tenor in ci_living_list:
        tenor = int(living_tenor.split(',')[0])
        living_rate = float(living_tenor.split(',')[1])
        for i in range(tenor):
            multiplier = multiplier*(1-living_rate/100)
            principal_living[index] = principal_living[index] * multiplier
            living.append(principal_living[index-1] * living_rate / (100-living_rate))
            index+=1
    # if living expense is less than compounding expense years.
    for _ in range(index,len(principal_living)):
        principal_living[index] = principal_living[index] * multiplier
        living.append(0)
    return principal_noliving, principal_living,living

#x, y, z = calculator("5,50;5,20","9,2",1000)
#print(x)
#print(y)
#print(z)