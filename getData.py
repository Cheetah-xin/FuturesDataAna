import pandas as pd
import numpy as np
import tushare as ts
import pandas_datareader as pdr
import yfinance as yf
import akshare as ak
from datetime import datetime
    

"""get data from pandas_datareader
def getdata(future_code='AAPL',
            start_day=datetime(2025,3,24),
            end_day=datetime(2025,3,24),
            ):
    data = pdr.get_data_yahoo(future_code,start_day,end_day)
    print(data.head())

def getdata2(future_code='AAPL',
             start_day='2025-03-01',
             end_day='2025-03-02'):
    data = yf.download(future_code,start=start_day,end=end_day)
    return data
"""
def get_futures_minute_data(symbol):
    futures_zh_minute_sina_df = ak.futures_zh_minute_sina(symbol=symbol, period="1")
    return futures_zh_minute_sina_df

if __name__=="__main__":
    symbol = 'RM2505'  # 期货合约代码
    data = get_futures_minute_data(symbol)
    filename = symbol+".csv"
    data.to_csv(filename)
    
    

