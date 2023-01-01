import yfinance as yf
import pandas as pd
import os

# trying to build a daily scanner, which informs if there are any good opportunities in call option for 20 stocks
# that i follow.
# Call options, ATM, 52 week low, 52 week high. Looking at 1yr options. WHat if Stock goes back to its 52 week high level.
# Or Stock goes 50% higher.

def getSNP500stocklist():
    table = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    df = table[0]
    df.to_csv('S&P500-Info.csv')
    df.to_csv("S&P500-Symbols.csv", columns=['Symbol'])
    return df['Symbol'].tolist()


def get52weekLow(stocks_list=[]):
    if len(stocks_list) == 0:
        stocks_list = getSNP500stocklist()
    #stocks_list = ['TSLA', 'Z', 'COIN', 'ZOOM', 'TDOC', 'U', 'ROKU', 'SPOT', 'TWLO', 'SQ','ARKK']
    #data = yf.download(stocks_list, start="2021-01-01", end="2022-12-31")['Close']
    snp52weekLow_df = pd.DataFrame(index=stocks_list,columns=['Close','Low','High','perc_from_high'])
    for stock in stocks_list:
        ticker = yf.Ticker(stock)
        snp52weekLow_df.loc[stock]['High']=ticker.info['fiftyTwoWeekHigh']
        snp52weekLow_df.loc[stock]['Low'] = ticker.info['fiftyTwoWeekLow']
        snp52weekLow_df.loc[stock]['Close'] = ticker.info['regularMarketPrice']
    snp52weekLow_df['perc_from_high'] = (snp52weekLow_df['Close'] - snp52weekLow_df['High']) / snp52weekLow_df[
        'High'] * 100
    #['Low']= data.min()
    #snp52weekLow_df['High'] = data.max()
    #snp52weekLow_df['Close'] = data.iloc[-1:].T.max(axis=1)

    return snp52weekLow_df.sort_values(['perc_from_high'], ascending=True)

#print(get52weekLow(['TSLA','Z']))
#get52weekLow().to_csv(os.getcwd() + "/option_data_dump.csv")

def getOptionPrice(stock,expiry=None,strike=None,type='call'):
    ticker = yf.Ticker(stock)
    if expiry is None:
        if type == 'call':
            option_df = ticker.option_chain().calls
        else:
            option_df = ticker.option_chain().puts
    else:
        list_expiry = list(filter(lambda x: expiry in x, ticker.options))
        if len(list_expiry) == 0:
            return None
        expiry = list_expiry[0]
        if type=='call':
            option_df = ticker.option_chain(expiry).calls
        else:
            option_df = ticker.option_chain(expiry).puts
    if strike is None:
        # look for whole number strike which is in the money.
        option_df = option_df[(option_df.inTheMoney == False)]
        option_df = option_df[option_df.strike == option_df.strike.astype(int)]
    else:
        option_df = option_df[option_df.strike == strike]
    option_df['ticker']=stock
    return option_df




def options_data_filter(stocks_list,expiry,strike=None):
    option_df = pd.DataFrame()
    snp52weekLow_df = get52weekLow(stocks_list)
    for stock in stocks_list:
        if strike is None:
            temp_df = getOptionPrice(stock,expiry,strike)
        else:
            temp_df = getOptionPrice(stock, expiry, strike).iloc[0]
        if temp_df is not None:
            option_df = option_df.append(temp_df)
    option_df.set_index('ticker',inplace=True)
    option_df = option_df[[ 'strike', 'lastPrice', 'volume','openInterest']]
    option_df = snp52weekLow_df.join(option_df)
    #print(option_df)

    option_df['high_return'] = (option_df['High'] - (option_df['strike'] + option_df['lastPrice'])) / option_df['lastPrice']
    option_df['30pec_return'] = (option_df['Close'] * 1.3 - (option_df['strike'] + option_df['lastPrice'])) / option_df['lastPrice']
    option_df['50pec_return'] = (option_df['Close'] * 1.5 - (option_df['strike'] + option_df['lastPrice'])) / option_df[
        'lastPrice']
    option_df['100pec_return'] = (option_df['High'] * 2 - (option_df['strike'] + option_df['lastPrice'])) / option_df[
        'lastPrice']
    return option_df.sort_values(['high_return'], ascending=False)


stocks_list = ['TSLA', 'Z', 'COIN', 'TDOC', 'U', 'ROKU', 'SPOT', 'TWLO', 'SQ', 'SHOP', 'ZM', 'ARKK',

               'ETSY', 'PYPL', 'NVDA']

stocks_list1 = ['TDOC', 'U', 'ROKU', 'TWLO', 'SQ', 'ZM', 'ETSY', 'PYPL', 'ATVI']

#print(options_data_filter(stocks_list,'2023-01').to_string())
print(getOptionPrice('TSLA','2023-01').to_string())
print(options_data_filter(['TSLA'],'2023-01').to_string())
#options_data_filter(['TSLA'],'2023-01').to_csv(os.getcwd() + "/option_data_dump1.csv")
#option_df.to_csv(os.getcwd() + "/option_data_dump.csv")

