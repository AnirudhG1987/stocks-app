
def calculator(ci_script,ci_living,amount):
    ci_list = ci_script.split(';')
    ci_living_list = ci_living.split(';')

    principal_noliving = []
    principal_living = []
    living = []
    principal_living.append(amount)
    principal_noliving.append(amount)
    living.append(0)

    for ci_teno32rr in ci_list:
        tenor = int(ci_tenor.split(',')[0])
        rate = float(ci_tenor.split(',')[1])
        for i in range(tenor):
            principal_noliving.append(principal_noliving[-1] * (1 + rate / 100))
            principal_living.append(principal_living[-1] * (1 + rate / 100)*(1-ci_living/100))
            living.append(principal_living[-1] * (ci_living / 100))

    return principal_noliving, principal_living,living