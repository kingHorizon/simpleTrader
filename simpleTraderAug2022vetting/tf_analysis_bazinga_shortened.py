#%pip install requests_cache
#%pip install pandas==1.3.5
import yfinance as yf
import datetime, os, sys, math, time, pytz
import pandas as pd
import numpy as np
import finta as fta
import itertools
from scipy.signal import argrelextrema
#import requests_cache
def main(sym='SPY',interval="1d",period='max',start=None,end=None,candle_range=None):
    # possible periods: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max
    # possible intervals: 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo
    # sanitize paramters
    if period =='max' and (('m' in interval and 'o' not in interval) or ('h' in interval)):
        if interval in ['2m','5m','10m','15m']:
            period = '1mo'
            print('period',period)
        elif interval == '1m':
            period = '5d'
        else: #YYYY-MM-DD
            dtnow=datetime.datetime.utcnow()
            end=dtnow.strftime('%Y-%m-%d')
            start= (dtnow - datetime.timedelta(days=55)).strftime('%Y-%m-%d')
            period=None
            print('new interval',start,end)
    #get price data for symbol
    ticker = yf.Ticker(sym)
    df = ticker.history(period=period,interval = interval,start=start,end=end)
    time.sleep(1)
    #print(type(df))
    #print(df.columns) # NOTE first letter of column names are capitlaized 
    #print(f'\033[1;32;40m WARNING !!!!! first letter of column names are capitlaized \033[0;37;40m ')
    df = df.rename(columns={'Open':'open','Close':'close','High':'high','Low':'low','Volume':'volume'})
    df['datetime']=dts=list(pd.to_datetime(df.index))
    dtn = dts[0]
    if dtn.tzinfo is None or dtn.tzinfo.utcoffset(dtn) is None:
        print('naive datetimes converted to utc')
        df['datetime']=list(pd.to_datetime(df.index,utc=True))
    tot_len = len(df['datetime'])
    if candle_range==None:
        candle_range = tot_len
    if tot_len-1-candle_range < 0:
        raise ValueError('not enough candles available online')
    df = df.loc[df.index[tot_len-1-candle_range]:,:]
    if len(df['datetime']) < candle_range:
        raise ValueError('not enough candles available online')
    #print('not anymore')
    #print(df.columns)
    df_d = {} # to house non singleton analysis data about indicators and time series
    
    
    
    ###
    ###
    ###
    
    
    
    #get signals
    cls,ops,lws,hhs,vls = df['close'],df['open'],df['low'],df['high'],df['volume']
    # - rsi
    def rsi(df,rsi_len=21):
        df['rsi'] = fta.TA.RSI(df,rsi_len)
    # -- hammer
    def hammer(df,cls,ops,hhs,lws,wick_to_body_ratio=2,wick_to_wick_ratio=1.5):
        hmrs=[]
        uphs,dwnhs=[],[]
        for i,h0 in enumerate(hhs):
            bod=cls[i]-ops[i]
            l0,cl0,op0=lws[i],cls[i],ops[i]
            try:
                if bod<0: # down candle
                    
                    uph = abs(l0-cl0)/abs(h0-op0) # up/bull signal
                    dwnh = abs(h0-op0)/abs(l0-cl0)
                elif bod>0: # up candle
                    uph = abs(l0-op0)/abs(h0-cl0)
                    dwnh = abs(h0-cl0)/abs(l0-op0)
                else:
                    hmrs.append(0)
                    continue
                if uph > wick_to_wick_ratio :
                    wick_size= (min(ops[i],cls[i])-l0) #lower :NOTE should be positive
                    if abs(wick_size) / abs(bod) >  wick_to_body_ratio:
                        expected_percent_change = (wick_size+abs(bod))/cl0
                        hmrs.append(expected_percent_change)
                    else:
                        hmrs.append(0)
                elif dwnh > wick_to_wick_ratio:
                    wick_size= (max(ops[i],cls[i])-h0) # upper # NOTE should be negative
                    if abs(wick_size) / abs(bod) >  wick_to_body_ratio:
                        expected_percent_change = (wick_size-abs(bod))/cl0
                        hmrs.append(expected_percent_change)
                    else:
                        hmrs.append(0)
                else:
                    hmrs.append(0)
            except:
                hmrs.append(0)
        df['hammers'] = hmrs
        #print(hmrs,'hammers')
    def sentiment(df,df_d):
        #https://medium.datadriveninvestor.com/sentiment-analysis-of-stocks-from-financial-news-using-python-82ebdcefb638?gi=a8849e546f46
        df['sentiments'] = [0]*len(df['hammers'])
        print('WARNING - Sentiments analysis not yet implemented')
        pass










    
    #NOTE every comment line below should have a corresponding function , if not assume this script is incomplete. For instance sub categories should have functions and parent categories should have functions that execute a custom grouping of its subcategory functions again , redundant but for compeltion. for instance a function to replace the price data retrieval method is not complete.
    #get price data for symbol
    #get signals
    # -common Technical Analysis
    rsi(df,rsi_len=7)
    # -extrema
    #extrema(df,n=5)
    # -candle patterns
    # -- engulfing
    #engulfing(df,cls,ops)
    # -- hammer
    hammer(df,cls,ops,hhs,lws,wick_to_body_ratio=2,wick_to_wick_ratio=1.5)
    # -- stars
    # -- tweezers
    # -- rest
    # -- soldiers
    # -- gap
    #gap(df,ops,cls,ATR_tol=.075)
    # -key levels
    # -- s/r levels
    #support_resistance_levels(df,df_d,hhs,lws,ops,cls,touches=2,ATR_tol=.1,ATR_reaction=2,level_suspects=None)
    # -- s/r/balance zones
    # -- trend lines
    # - market structure
    # -- trend lines
    # -- patterns
    # --- head and shoulders
    # --- double top/bottom
    #double_bottoms_and_tops(df,hhs,lws,ops,cls)
    # --- pennants 
    # --- flags
    # --- wedges
    # -sentiment
    sentiment(df,df_d)
    #get mtf bullish/bearish sequences
    # - connected, higher tf, specific signals
    
    #print(df.columns)
    print(f'\033[1;34;40m symbol: {sym} timeframe: {interval}\033[0;37;40m')
    print('hammer signals:\n',df['hammers'][-10:])
    print('current sentiment score (timeframe unknown... max data pulled):\n', df['sentiments'][-1:])
    print(f'\033[1;33;40m {sym} timeframe {interval} current trade reccomendation:\n', df['hammers'][-1],'\n\033[0;37;40m')
    # NOTE this function sends data up to a ranking function that takes inputs for how to weight each indicator signal and aggregates them into a tradeable prediction about price movement 
    return df,df_d
def bazinga_test():
    print(f'\033[1;34;40m Welcome to tf_analysis_bazinga_shortened.py \033[0;37;40m \n')
    print('\033[1;33;40m trade reccomendations are in yellow \033[0;37;40m')
    print(f'\033[1;32;40m Positive value for a date/time stamp means buy \033[0;37;40m')
    print(f'\033[1;31;40m Negative value for a date/time stamp means sell \033[0;37;40m \n')
    tf = '1d' # candle timeframe size to test. best options: '1d' daily candles and '1h' hourly candles and '15m' 15 minute candles # NOTE period range for candles is automaticaly set to the maximum and pared down using the candle_range parameter. 
    symbols = ['SPY','TSLA','V','MPC','MSFT']
    candle_range = 100 # number of most recent candles to analyze 
    master_df={}
    for sym in symbols:    
        master_df[sym] = main(sym,interval=tf,candle_range=100)
        pass
    print('*done*')
    return master_df
bazinga_test()