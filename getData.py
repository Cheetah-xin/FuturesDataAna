import pandas as pd
import numpy as np
import akshare as ak
from datetime import datetime
import re
    

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
def get_futures_daily_data(symbol, start,end):
    futures_daily_df = ak.futures_zh_daily_sina(symbol=symbol)
    return futures_daily_df

if __name__=="__main__":
    symbol_set={"RM2505","OI2505","m2505","ni2505"}
    # minite
    for symbol in symbol_set:
        try:
            data = get_futures_minute_data(symbol)
            start=data['datetime'].min()
            start_str = re.sub(r'[ :-]', '',start)
            end = data['datetime'].max()
            end_str = re.sub(r'[ :-]', '',end)
            filename_minute = "./download_data/{symbol}_min_{start}_{end}.csv".format(symbol=symbol,start=start_str,end=end_str)
            data.to_csv(filename_minute,index=False)
        except Exception as e:
            print (e)
            continue

    # daily
    for symbol in symbol_set:
        try:
            data = get_futures_daily_data(symbol=symbol)
            filename_daily = "./download_data/{symbol}_daily.csv".format(symbol=symbol)
            data.to_csv(filename_daily)
        except Exception as e:
            print(e)
            continue

