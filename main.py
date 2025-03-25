import pandas as pd
import numpy as np
import seaborn as sn
from stockstats import StockDataFrame
import datetime
import matplotlib.pyplot as plt


filename = "../RawData/SHFE.NI.CSV"
df = pd.read_csv(filename)
stock_data = StockDataFrame.retype(df)
print(df.columns)
df.describe()
df['y'] = df['datetime'].map(lambda x: x[:4])
pass
