import yfinance as yf
from sympy import symbols, solve
import numpy as np

def getstockdata(ticker,period,freq):
    ticker = yf.Ticker(ticker)
    if period == "100":
        tsla_df = ticker.history(period="max", interval=str(freq) + "mo")
    else:
        tsla_df = ticker.history(period=period+"y",interval = str(freq)+"mo")
    tsla_df.dropna(subset = ['Close'], inplace=True)
    return tsla_df['Close']

#print(stock_data('AAPL',"10","3"))

def cagr(amount, networth, years):
    x = symbols('x')
    expr = (1+x)**(years)-1-x*(networth/amount)

    sol = solve(expr)
    for x in sol:
        if x>0:
            return x


print(cagr(100,352732,10))


