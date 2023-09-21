import math

import numpy as np
from math import log

def s_curve_adoption(total_market, percentage_change, years):
    def sigmoid(x):
        return 1 / (1 + np.exp(-x))

    market_share = []
    mid_point = years / 2
    z_intial = -log((100/(50-0.5*percentage_change))-1,math.e)
    z_final = -log((100 /(50+0.5* percentage_change)) - 1, math.e)
    for year in range(1, years + 1):
        x = (z_final-z_intial) * (year - mid_point) / years
        share =  round(total_market*(sigmoid(x) - sigmoid(z_intial)) / (sigmoid(z_final) - sigmoid(z_intial)),2)
        market_share.append(share)
    # Calculate yearly sales

    return market_share

def optimus_bot_revenue_model(max_subscription_fee, max_hours_per_day, max_days_per_year, max_bot_produced,years):
    cumulative_bots_produced = 0
    revenue_list = []
    subscription_fee_list = s_curve_adoption(max_subscription_fee,99,years)
    hours_per_day_list = s_curve_adoption(max_hours_per_day, 99, years)
    days_per_year_list = s_curve_adoption(max_days_per_year, 99, years)
    yearly_bot_production = s_curve_adoption(max_bot_produced, 99, years)


    for year, subscription_fee in enumerate(subscription_fee_list):
        cumulative_bots_produced += yearly_bot_production[year]
        revenue = cumulative_bots_produced * subscription_fee_list[year] * hours_per_day_list[year] * days_per_year_list[year]
        revenue_list.append(round(revenue/1000,2))

    return revenue_list

revenue_list = optimus_bot_revenue_model(25,20,300,20,20)
print("Revenue List:", revenue_list)


#print(s_curve_adoption(20,0.1,99.9,30))
#print(s_curve_adoption(20,99.8,20))