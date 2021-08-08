import ast
from datetime import datetime

import yfinance as yf
from yfinance import shared
from sympy import symbols, solve
import pandas as pd
import requests
import io

def getSNP500stocklist():
    table = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    df = table[0]
    df.to_csv('S&P500-Info.csv')
    df.to_csv("S&P500-Symbols.csv", columns=['Symbol'])
    return df['Symbol'].tolist()


def getstockdata(tickers,date):
    Symbols = tickers

    start = date
    end = date

    stock_final = pd.DataFrame()
    # iterate over each symbol
    for i in Symbols[:10]:

        # print the symbol which is being downloaded
        print(str(Symbols.index(i)) + str(' : ') + i, sep=',', end=',', flush=True)

        try:
            # download the stock price
            stock = []
            stock = yf.download(i, start=start, end=end, progress=False)

            # append the individual stock prices
            if len(stock) == 0:
                None
            else:
                stock['Name'] = i
                stock_final = stock_final.append(stock, sort=False)
        except Exception:
            print("exception in ",i)
            None
    return stock_final[['Name','Close']]

def creatingdatabase():
    df_array = []
    for i in range(2000,2022):
        #date = pd.date_range('1/1/'+str(i), '1/10/'+str(i), freq='BMS')[0]
        #print(date)
        df_temp = getstockdata(getSNP500stocklist(), datetime.datetime(i,1,6))
        print("year is ",i)
        print(df_temp)
        if not df_temp.empty:
            df_array.append(df_temp.rename(columns = {'Close': i}))
    print(df_array)

def datadump():
    data = yf.download(getSNP500stocklist(), start="2000-01-01", end="2021-12-31")['Close']
    data.to_csv("templates/Stock_data_dump.csv")

#datadump()

def revenuedump():
    ticker = yf.Ticker('TSLA')
    print(ticker.earnings)
    #for stock in getSNP500stocklist()[0:1]:
    #    ticker = yf.Ticker(stock)
    #    print(ticker.earninTSLAgs)

#revenuedump()
#chutiya()

def getrevenuegrowthforallstock(start_year,end_year):
    stock_df = pd.read_csv("templates/Stock_data_dump1.csv")
    return_dict = {}
    df_date = stock_df['Date']
    for stock in stock_df.columns[1:]:
        #print(stock)
        df_stock = stock_df[stock]
        first_loc = df_stock.first_valid_index()
        last_loc = df_stock.last_valid_index()
        first_date = datetime.strptime(df_date.loc[first_loc], '%d/%m/%Y')
        last_date = datetime.strptime(df_date.loc[last_loc], '%d/%m/%Y')
        first_stock_price = df_stock.loc[first_loc]
        last_stock_price = df_stock.loc[last_loc]
        return_dict[stock]=((last_stock_price/first_stock_price)**(365/(last_date-first_date).days)-1)*100

    returns_df = pd.DataFrame(dict(sorted(return_dict.items(), key=lambda item: item[1], reverse=True)),index=[0])
    return returns_df.transpose()


def getreturnsforallstock(start_year,end_year):
    stock_df = pd.read_csv("templates/Stock_data_dump1.csv")
    return_dict = {}
    df_date = stock_df['Date']
    for stock in stock_df.columns[1:]:
        #print(stock)
        df_stock = stock_df[stock]
        first_loc = df_stock.first_valid_index()
        last_loc = df_stock.last_valid_index()
        first_date = datetime.strptime(df_date.loc[first_loc], '%d/%m/%Y')
        last_date = datetime.strptime(df_date.loc[last_loc], '%d/%m/%Y')
        first_stock_price = df_stock.loc[first_loc]
        last_stock_price = df_stock.loc[last_loc]
        return_dict[stock]=((last_stock_price/first_stock_price)**(365/(last_date-first_date).days)-1)*100

    returns_df = pd.DataFrame(dict(sorted(return_dict.items(), key=lambda item: item[1], reverse=True)),index=[0])
    return returns_df.transpose()

def getallstockdata():
    url = "https://pkgstore.datahub.io/core/nasdaq-listings/nasdaq-listed_csv/data/7665719fb51081ba0bd834fde71ce822" \
          "/nasdaq-listed_csv.csv "
    s = requests.get(url).content
    companies = pd.read_csv(io.StringIO(s.decode('utf-8')))
    Symbols = companies['Symbol'].tolist()
    print(Symbols)

    start = datetime.datetime(2020, 8, 1)
    end = datetime.datetime(2021, 8, 1)

    # create empty dataframe
    stock_final = pd.DataFrame()
    # iterate over each symbol
    for i in Symbols:

        # print the symbol which is being downloaded
        print(str(Symbols.index(i)) + str(' : ') + i, sep=',', end=',', flush=True)

        try:
            # download the stock price
            stock = []
            stock = yf.download(i, start=start, end=end, progress=False)

            # append the individual stock prices
            if len(stock) == 0:
                None
            else:
                stock['Name'] = i
                stock_final = stock_final.append(stock, sort=False)
        except Exception:
            print("exception in ",i)
            None
    print(stock_final)

def getstockdata(ticker,period,freq):
    ticker = yf.Ticker(ticker)
    if period == "100":
        tsla_df = ticker.history(period="max", interval=str(freq) + "mo")
    else:
        tsla_df = ticker.history(period=period+"y",interval = str(freq)+"mo")
    tsla_df.dropna(subset = ['Close'], inplace=True)
    return tsla_df['Close']

def getstockdatarange(ticker,start, end,freq):
    tsla_df = yf.download(tickers = ticker, start=start+"-01-01",end=end+"-12-31",interval = str(freq)+"mo")
    tsla_df.dropna(subset = ['Close'], inplace=True)
    #print(tsla_df)
    if ticker in shared._ERRORS.keys():
        error_message = shared._ERRORS[ticker]
    else:
        error_message =''
    return tsla_df['Close'], error_message


def cagr(amount, networth, years):
    x = symbols('x')
    expr = (1+x)**(years)-x*(networth/amount)-1

    sol = solve(expr)
    for x in sol:
        if x>0:
            return x



