import pandas_datareader as pdr
import datetime as dt
import nasdaqdatalink
import pandas as pd

ticker = "TSLA"
start = dt.datetime(2010, 1, 1)
end = dt.datetime(2021, 12, 31)

#data = pdr.get_data_yahoo(ticker, start, end)

#print(data)
nasdaqdatalink.ApiConfig.api_key = "5MUxaRTRMk_C5sHfq5yB"
data = nasdaqdatalink.get_table('ZACKS/FC',ticker="AAPL" ,paginate=True)
print(data)
