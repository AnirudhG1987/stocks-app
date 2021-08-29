from datetime import datetime

import yfinance as yf
from sympy import symbols, solve
import pandas as pd
import requests
import numpy as np
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
    try:
        tsla_df = yf.download(tickers = ticker, start=start+"-01-01",
                              end=end+"-12-31",interval = str(freq)+"mo")
    except:
        print("we are here")
    tsla_df.dropna(inplace=True)
    if (len(ticker)==1):
        tsla_df = tsla_df['Close'].to_frame()
        tsla_df.columns = [ticker[0]]
        return tsla_df
    else:
        return tsla_df['Close']

def getstockportfoliodata(amount,ticker,start,end,freq):
    multiple_stock_data = getstockdatarange(ticker,start,end,freq)
    if len(multiple_stock_data) == 0:
        return multiple_stock_data
    dates_data = np.datetime_as_string(multiple_stock_data.index.values, unit='D')
    ts = pd.to_datetime(multiple_stock_data.index.values)
    d = ts.strftime('%Y-%m')
    #dates_data = [date.strptime( '%Y-%m') for date in multiple_stock_data.index.values]
    dates_data = d.values
    #dates_data.index = pd.to_datetime(dates_data.index, format='%Y-%m-%d')
    #dates_data.index = dates_data.index.strftime('%Y-%m')
    investment = [amount*(i+1) for i in range(len(dates_data))]
    #stocks_portfolio = []
    excel_data = pd.DataFrame({'Dates':dates_data})
    excel_data['Investment'] = investment
    for stock in multiple_stock_data.columns:
        ticker_yf = yf.Ticker(stock)
        dividends_df = ticker_yf.dividends
        dividends_df.index = pd.to_datetime(dividends_df.index, format='%Y-%m-%d')
        dividends_df.index = dividends_df.index.strftime('%Y-%m')
        stock_data = multiple_stock_data[stock]
        no_of_shares = []
        no_of_shares_nd = []
        dividends_list = []
        portfolio = []
        portfolio_nd = []
        no_of_shares.append(round(amount / stock_data[0], 2))
        no_of_shares_nd.append(round(amount / stock_data[0], 2))
        portfolio.append(round(no_of_shares[-1] * stock_data[0], 2))
        portfolio_nd.append(round(no_of_shares[-1] * stock_data[0], 2))
        dividends_list.append(0)
        for i in range(1, len(dates_data)):
            dividend_amount =0
            if dates_data[i] in dividends_df.index:
                dividend_amount = dividends_df.loc[dates_data[i]]*no_of_shares[-1]
            dividends_list.append(dividend_amount)
            no_of_shares.append(round((amount+dividend_amount) / stock_data[i] + no_of_shares[-1], 2))
            no_of_shares_nd.append(round((amount) / stock_data[i] + no_of_shares_nd[-1], 2))
            portfolio_nd.append(round(no_of_shares_nd[-1] * stock_data[i], 2))
            portfolio.append(round(no_of_shares[-1] * stock_data[i], 2))
        #stocks_portfolio.append(portfolio)
        excel_data[stock+' Shares']=no_of_shares
        # put a check box for dividennds
        #excel_data[stock + ' Portfolio ND']= portfolio_nd
        excel_data[stock + ' Portfolio'] = portfolio
        #excel_data['Dividends'] = dividends_list
    return excel_data

def cagr(amount, networth, years):
    x = symbols('x')
    expr = (1+x)**(years)-x*(networth/amount)-1

    sol = solve(expr)
    for x in sol:
        if x>0:
            return x


