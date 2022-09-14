### import modules and libraries ###
#%pip install requests_cache
#%pip install pandas==1.3.5
import yfinance as yf
import datetime, os, sys, math, time, pytz
import pandas as pd
import numpy as np
import finta as fta
import itertools
from scipy.signal import argrelextrema


def get_historical_trading_signals_for_symbol(sym='SPY',interval="1d",period='max',start=None,end=None,candle_range=None,signals=['hammer'],verbose=False):
    
    """ 
        DESCRIPTION :
        A short and sweet function that populates a pandas-dataframe (a table)
        with a user's preffered historical trade signals of a single equity-symbol.
        
        PARAMATER OPTIONS :
        - verbose : if True, will print information about function as it executes
        - periods: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max
        - intervals: 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo
        - candle_range : any integer
        - start : start date
        - end : end date
        - sym : symbol/ticker/equity to collect signals for 
        - signals : a list of strings representing a signal to be chosen from any of the following
            -- "hammer" : 
            -- "sentiment" : provides a value between -1 and 1 ranking the sentiment of news from over a time period 
                --- NOTE : not capable of collecting historical data yet. can only assign signal to the immediate day
        (these options are pulled from the yfinance python module. https://aroussi.com/post/python-yahoo-finance
        "m" is short hand for minute "d" is short for day, "mo" is month, "y" year, "ytd" year-to-date, 
        "max" maximum period for intraday intervals/timeframes/candle-lengths... which is approximately 30 days)
        
    """
    
    
    ##########################################
    #### initialize data and sanitize paramters
    ##########################################
    
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
    
    # rename the dataframe/table columns so that they are easier to work with 
    df = df.rename(columns={'Open':'open','Close':'close','High':'high','Low':'low','Volume':'volume'})
    # create a datetime object column for easier temporal manipulations
    df['datetime']=dts=list(pd.to_datetime(df.index))
    # convert datetime objects from datetime column to timezone aware datetime objects for easier temporal manipulations
    dtn = dts[0]
    if dtn.tzinfo is None or dtn.tzinfo.utcoffset(dtn) is None:
        print('naive datetimes converted to utc')
        df['datetime']=list(pd.to_datetime(df.index,utc=True))
        
    # make sure we have the desired number of candles
    tot_len = len(df['datetime'])
    if candle_range==None:
        candle_range = tot_len
    if len(df['datetime']) < candle_range:
        raise ValueError('not enough candles available online')

    df_d = {} # this variable will be used to keep non scalar analysis data about indicators and time series
    
    
    ##########################################
    ##########################################
    #### define historical signal generator functions
    ##########################################
    ##########################################
    
    
    ### make short hand for accessing dataframe/tablel columns
    cls, ops, lws, hhs, vls = df['close'],df['open'],df['low'],df['high'],df['volume']
    
    
    #############
    ### - "rsi" : relative strngth index - technical analysis
        def rsi(df,rsi_len=21):
            df['rsi'] = fta.TA.RSI(df,rsi_len)
            # END FUNCTION
        rsi(df,rsi_len=7)
        
    ############# 
    ### -- "hammer" - candle pattern signal
    if 'hammer' in signals:
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
            # END FUNCTION
        hammer(df,cls,ops,hhs,lws,wick_to_body_ratio=2,wick_to_wick_ratio=1.5)
        
    ############# 
    ### -- "sentiment" - qualitative analysis (news based)
    if "sentiment" in signals :
        def sentiment(df,df_d):
            #https://medium.datadriveninvestor.com/sentiment-analysis-of-stocks-from-financial-news-using-python-82ebdcefb638?gi=a8849e546f46
            df['sentiments'] = [0]*len(df['hammers'])
            print('WARNING - Sentiments analysis not yet implemented')
            pass
            # END FUNCTION
        sentiment(df,df_d)

    ##########################################
    #### Print function and signal information to user device (i.e. terminal)
    ##########################################
    #print(df.columns)
    print(f'\033[1;34;40m symbol: {sym} timeframe: {interval}\033[0;37;40m')
    print('hammer signals:\n',df['hammers'][-10:])
    print('current sentiment score (timeframe unknown... max data pulled):\n', df['sentiments'][-1:])
    print(f'\033[1;33;40m {sym} timeframe {interval} current trade reccomendation:\n', df['hammers'][-1],'\n\033[0;37;40m')
    # NOTE this function should send data up to a ranking function that takes inputs for how to weight each indicator signal and aggregate them into a tradeable prediction about price movement 
    return df,df_d
    
    
    ###
    ###
    ###
   

    ##########################################
    ##########################################
    #### NOTES AND ROADMAP
    ##########################################
    ##########################################
    # potential signals
    #get price data for symbol
    #get signals
    # -common Technical Analysis
    # -rsi
    # -extrema
    #extrema(df,n=5)
    # -candle patterns
    # -- engulfing
    #engulfing(df,cls,ops)
    # -- hammer
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
    #get multi-timeframe bullish/bearish sequences
    # - connected, higher tf, specific signals
    
    # END FUNCTION #

# main function executed when ran from terminal
if __name__ == "__main__":
    def bazinga_test(verbose=True):
        """
        
            this tester function will produce signals for the tickers ['SPY','TSLA','V','MPC','MSFT'] 
            over the past 100 days
            and print a trade signal for each symbol if available
            
        """
        
        if verbose :
            print(f'\033[1;34;40m Welcome to tf_analysis_bazinga_shortened.py \033[0;37;40m \n')
            print('\033[1;33;40m trade reccomendations are in yellow \033[0;37;40m')
            print(f'\033[1;32;40m Positive value for a date/time stamp means buy \033[0;37;40m')
            print(f'\033[1;31;40m Negative value for a date/time stamp means sell \033[0;37;40m \n')
            
        # initialize automatic/default paramters to test 
        tf = '1d' # candle timeframe size to test. best options: '1d' daily candles and '1h' hourly candles and '15m' 15 minute candles # NOTE period range for candles is automaticaly set to the maximum and pared down using the candle_range parameter. 
        symbols = ['SPY','TSLA','V','MPC','MSFT']
        candle_range = 100 # number of most recent candles to analyze 
        master_df={}
        
        # for each symbol/ticker generate signals
        for sym in symbols:    
            master_df[sym] = main(sym,interval=tf,candle_range=100,verbose=verbose)
            pass
        
        print('*done*')
        return master_df
        # END FUNCTION #
    
    bazinga_test()
