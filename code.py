#intraday strategy using GARCH model

#load both datasets, set indexes and calculate daily log returns
import matplotlib.pylot as plt
from arch import arch_model
from tqdm import tqdm
import pandas as pd
import numpy as np
import os 

data_folder = 'C:/Users/user/Desktop/Python Scripts'

daily_df = pd.read_csv(os.path.join(data_folder, 'simulated_daily_data.csv'))

daily_df['Date'] = pd.to_datetime(daily_df['Date']) #calculating date columns

daily_df = daily_df.set_index('Date') #assign as index 

daily_df['log-ret'] = np.log(daily_df['Adj Close']).dff() #log

#now that we have daily data, we need intraday data

intraday_5min_df = pd.read_csv(os.path.join(data_folder, '5min.csv'))

intraday_5min_df['datetime' = pd.to_datetime(5min_df['Date'])

#define function to fit GARCH model and predict 1-day ahead volatility in a rolling window
#autoregressive order of 1 then 3

daily_df['variance'] = daily_df['log_ret'].rolling(180).var() #variance of log return
daily_df['variance'].plot()




