from django.test import TestCase

# Create your tests here.
multiplier = 1
index = 1
for living_tenor in ci_living_list:
    tenor = int(living_tenor.split(',')[0])
    living_rate = float(living_tenor.split(',')[1])
    for i in range(tenor):
        multiplier = multiplier * (1 - living_rate / 100)
        if index < len(principal_living):
            principal_living[index] = principal_living[index] * multiplier

        else:
            principal_living.append(principal_living[-1] * (1 - living_rate / 100))
            principal_noliving.append(principal_noliving[-1])
            living.append(principal_living[-1] * living_rate / 100)
        index += 1
# if living expense is less than compounding expense years.
# then constant expenses
living_multiplier = 1
sum = 0
for ci_tenor in ci_list:
    tenor = int(ci_tenor.split(',')[0])
    sum += tenor
    if sum > index:
        break
for i in range(index, len(principal_living)):
    print(principal_living[i - 1])
    print(living[-1])
    print(multiplier)
    print(1 - living_rate / 100)
    principal_living[i] = principal_noliving[i - 1] * multiplier / (1 - living_rate / 100) - living[-1]
    living.append(living[-1])