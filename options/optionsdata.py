import yfinance as yf
from datetime import date
from datetime import datetime
import pandas as pd
import math


def get_delta(expiry):
    d0 = date.today()
    d1 = datetime.strptime(expiry, '%Y-%m-%d')
    delta = (d1.date() - d0).days
    return delta


def rate_of_return_calc(spot,strike,option_cost,expiry):
    total_cost = strike+option_cost
    delta = get_delta(expiry)
    #print("this is profit",spot,total_cost,option_cost,delta)
    profit = spot - total_cost
    #print(profit,option_cost,delta)
    return_on_capital = max((((profit / option_cost) ** (365 / delta)) - 1) * 100,0)
    if return_on_capital != return_on_capital:
        return_on_capital = 0

    #print(return_on_capital)
    return round(return_on_capital,2)

# Generic Dataframe creator for varying spot vs expiry vs strike
def get_options_dataframe(ticker,ror):
    ticker = yf.Ticker(ticker)
    #print(ticker.options)
    rate_of_return = ror
    #print(ror)
    current_price = ticker.history(period="1d")['Close'].values[0]
    #print(current_price)
    return_df = pd.DataFrame(columns=["Expiry", "Strike", "Option Cost", "Total Cost", "Stock Price","Return on Capital"])
    for expiry in ticker.options:
        opt_chain = ticker.option_chain(expiry)
        option_df = opt_chain.calls
        #itm_filter =  option_df['inTheMoney']==False
        sum_column = option_df["strike"] + option_df["lastPrice"]
        option_df["PricetoPay"] = sum_column
        #print(option_df)
        for i in range(len(option_df)):

            strike = option_df["strike"].iloc[i]
            total_cost = option_df["PricetoPay"].iloc[i]
            option_cost = option_df["lastPrice"].iloc[i]
            delta = get_delta(expiry)
            price_in_future = current_price * (1 + rate_of_return) ** (delta / 365)
            return_on_capital = rate_of_return_calc(price_in_future, strike, option_cost, expiry)
            #print(expiry,strike,total_cost,price_in_future,profit,delta,return_on_capital)
            to_append = [expiry,strike,option_cost,total_cost,price_in_future,return_on_capital]
            if return_on_capital>0 and not math.isinf(return_on_capital) and strike<1.5*current_price and strike>0.5*current_price:
                #print(price_in_future, profit, option_cost, delta)
                df_length = len(return_df)
                return_df.loc[df_length] = to_append
                #print(option_df[itm_filter]["PricetoPay"].iloc[0]/(expiry-))
    #print(return_df)
    #return_df.plot(x ='Strike', y='Return on Capital', kind = 'line')
    #plt.show()
    return return_df

# Chart No 1 comparing ror w.r.t strike for varying expiry
def get_ror_strike_per_expiry_df(options_df):
    expiry_list = options_df['Expiry'].unique()
    strike_list = options_df['Strike'].unique()
    #print(expiry_list)
    chart_column_list = ["Strike"]+[x for x in expiry_list]
    #chart_column_list = [x for x in expiry_list]
    #print(chart_column_list)
    ror_strike_df = pd.DataFrame(columns=chart_column_list)
    for strike in strike_list:
        to_append = [strike] +  [0 for x in expiry_list]
        # print(to_append)
        df_length = len(ror_strike_df)
        ror_strike_df.loc[df_length] = to_append

    #print(ror_strike_df)
    for expiry in expiry_list:
        expiry_filtered_df =  options_df.loc[options_df['Expiry'] == expiry]
        #print(expiry_filtered_df)
        for strike in expiry_filtered_df['Strike']:
            ror_strike_df.loc[ror_strike_df['Strike']==strike,expiry] = \
                expiry_filtered_df.loc[expiry_filtered_df['Strike'] == strike]['Return on Capital'].values[0]
    return ror_strike_df

# Chart No 3 comparing ror w.r.t spot for a varying expiry for a particular strike
def get_ror_spot_per_expiry_df(ticker,strike,rate):
    ticker = yf.Ticker(ticker)
    current_price = ticker.history(period="1d")['Close'].values[0]
    expiry_list = ticker.options
    expiry_list= list(filter(lambda x:  get_delta(x)>360 ,expiry_list))
    chart_column_list = ["spot"]+[x for x in expiry_list]
    ror_strike_df = pd.DataFrame(columns=chart_column_list)
    spot_list = [round(current_price * (1 + rate) ** i, 0) for i in range(4)]
    for spot in spot_list:
        to_append = [spot] +  [0 for x in expiry_list]
        df_length = len(ror_strike_df)
        ror_strike_df.loc[df_length] = to_append

    for expiry in expiry_list:
        opt_chain = ticker.option_chain(expiry)
        option_df = opt_chain.calls
        #print(option_df)
        for spot in spot_list:

            if strike in option_df['strike'].values:
                option_cost = option_df.loc[option_df['strike'] == strike]["lastPrice"].values[0]
                ror_strike_df.loc[ror_strike_df['spot'] == spot, expiry] = \
                rate_of_return_calc(spot, strike, option_cost, expiry)
    return ror_strike_df


# Chart No 2 comparing ror w.r.t strike for varying spot for a particular expiry
def get_ror_strike_per_spot_df(ticker,expiry,rate):
    ticker = yf.Ticker(ticker)
    current_price = ticker.history(period="1d")['Close'].values[0]
    opt_chain = ticker.option_chain(expiry)
    option_df = opt_chain.calls
    #sum_column = option_df["strike"] + option_df["lastPrice"]
    #option_df["PricetoPay"] = sum_column
    spot_list = [round(current_price*(1+rate)**i,0) for i in range(5)]
    chart_column_list = ["strike"]+[str(x) for x in spot_list]
    #print(chart_column_list)
    ror_spot_df = pd.DataFrame(columns=chart_column_list)
    strike_list = option_df['strike'].unique()
    for strike in strike_list:
        if strike > 0.5*current_price and strike < 1.5*current_price:
            to_append = [strike] + [0 for _ in spot_list]
            # print(to_append)
            df_length = len(ror_spot_df)
            ror_spot_df.loc[df_length] = to_append
    #print(ror_spot_df)
    for strike in strike_list:
        for spot in spot_list:
            option_cost = option_df.loc[option_df['strike']==strike]["lastPrice"].values[0]
            ror_spot_df.loc[ror_spot_df['strike']==strike,str(spot)] = \
                    rate_of_return_calc(spot,strike,option_cost,expiry)

    return ror_spot_df

#print(get_ror_spot_per_expiry_df('TSLA',850,0.7))
#print(get_ror_strike_per_spot_df('TSLA','2023-06-16'))
#print(get_options_dataframe("TSLA",0.5))
#get_ror_strike_per_expiry_df(get_options_dataframe('TSLA',0.5))