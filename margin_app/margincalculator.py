#
# It calculates the values of three lists over time, given specific input parameters:
#
# int_script: A string containing semi-colon separated tenors and interest rates (e.g., "2,4.5;3,5.0" means a 4.5% interest rate for 2 periods followed by a 5.0% interest rate for 3 periods)
# living_growth_script: A string containing semi-colon separated tenors and living growth rates (e.g., "2,3;3,4" means a 3% living growth rate for 2 periods followed by a 4% living growth rate for 3 periods)
# initial_living_amount: The initial living amount
# initial_borrowing_amount: The amount borrowed initially
#
# The function calculates three lists over time:
#
# yearly_living: This list contains the value of the initial_living_amount over time by considering the growth rate from living_growth_script
#
# interest_paid: This list contains the interest paid over time by considering the interest rate from int_script. Interest is calculated using the formula
#
# interest_paid[i]=(yearly_living[i]/2+total_borrowing[i-1])*interest[i]
#
# for the first entry of total_borrowing please use initial_borrowing_amount
#
# total_borrowing: This list contains the total borrowing which is calculated as
# total_borrowing[i]=total_borrowing[i-1]+interest_paid[i]+yearly_living[i]
#
# Here is an overview of the function:
#
# int_script_list and living_growth_script_list are created by splitting the input strings int_script and living_growth_script by semi-colons, respectively.
#
# yearly_living, interest_paid, and total_borrowing lists are initialized with their initial values initial_living_amount , 0,  and initial_borrowing_amount respectively.
#
# The interest rates and living growth rates are extracted from the input strings and stored in two NumPy arrays interest_rate_array and growth_rate_array.
#


import numpy as np

def margin_calculator(inv_script,int_script, living_growth_script,
                      shares,stock,initial_living_amount, initial_borrowing_amount,margin_shares):
    int_script_list = int_script.split(';')
    inv_script_list = inv_script.split(';')
    living_growth_script_list = living_growth_script.split(';')

    initial_investment_amount = shares*stock
    interest_paid = []
    interest_paid_margin =[]
    total_borrowing = [initial_borrowing_amount]
    shares_no_margin = [26518]
    #shares_no_margin = [shares-initial_borrowing_amount/stock]
    shares_on_margin = shares + margin_shares
    total_borrowing_margin = [initial_borrowing_amount+margin_shares*stock]
    current_investment = []
    investment_with_living = []
    investment_margin=[]
    interest_rate_array = np.empty(0)
    stock_price_growth = [stock]
    liv_growth_rate_array = np.empty(0)

    for int_tenor in int_script_list:
        tenor = int(int_tenor.split(',')[0])
        rate = float(int_tenor.split(',')[1])
        interest_rate_array = np.append(interest_rate_array, np.full(tenor, rate))

    for living_growth_tenor in living_growth_script_list:
        tenor = int(living_growth_tenor.split(',')[0])
        rate = float(living_growth_tenor.split(',')[1])
        liv_growth_rate_array = np.append(liv_growth_rate_array, np.full(tenor, rate))

    for inv_growth_tenor in inv_script_list:
        tenor = int(inv_growth_tenor.split(',')[0])
        rate = float(inv_growth_tenor.split(',')[1])
        for _ in range(tenor):
            stock_price_growth.append(stock_price_growth[-1]*(1+rate/100))

    yearly_living = [initial_living_amount]

    for i in range(len(liv_growth_rate_array)):
        interest = (yearly_living[i] / 2 + total_borrowing[i]) * interest_rate_array[i] / 100
        yearly_living.append(yearly_living[-1] * (1 + liv_growth_rate_array[i] / 100))
        interest_paid.append(interest)
        interest_margin = (yearly_living[i] / 2 + total_borrowing_margin[i]) * interest_rate_array[i] / 100
        interest_paid_margin.append(interest_margin)
        total_borrowing.append(total_borrowing[i] + interest + yearly_living[i])
        total_borrowing_margin.append(total_borrowing_margin[i] + interest_margin + yearly_living[i])
        current_investment.append(shares*stock_price_growth[i] - total_borrowing[i])
        investment_margin.append(shares_on_margin*stock_price_growth[i] - total_borrowing_margin[i])
        investment_with_living.append(shares_no_margin[i]*stock_price_growth[i]-yearly_living[-1])

        shares_no_margin.append(shares_no_margin[i]-yearly_living[-1]/stock_price_growth[i])

    return yearly_living, interest_paid, interest_paid_margin,total_borrowing, total_borrowing_margin,\
        current_investment, investment_with_living, investment_margin, stock_price_growth



#x,y,z = margin_calculator("10,6","5,10;5,20",140000,680000)
#print(x)
#print(y)
#print(z)