import vectorbt as vbt
import pandas as pd
import numpy as np
import datetime

end = datetime.datetime.now()
start = end - datetime.timedelta(days=2)

btc_price = vbt.YFData.download(
	["BTC-USD","ETH-USD"],
	missing_index='drop',
	start= start,
	end=end,
	interval="1m"
	).get("Close")

#This is custom indicator funtion
def custom_indicator(close, rsi_window = 14, ma_window = 50 ):
    print(type(close))
    #close is list of list (if mutiple price data pointed)
    rsi = vbt.RSI.run(close, window = ma_window).rsi.to_numpy()
    #ma is getting as pandasDataFrame
    ma = vbt.MA.run(close, window = ma_window).ma
    ma = ma.to_numpy()
    
    
    print(type(ma))
    print(ma)
    
    trend = np.where((rsi > 70) & (close > ma), -1, 0)
    trend = np.where((rsi < 30) & (close < ma), 1 , trend)
    print("printing trend values")
    print(trend)
    
    
    
    return trend

#Indicator factory
ind = vbt.IndicatorFactory(
        class_name = "Combination",
        short_name = "comb",
        input_names = ["close"],
        param_names = ["window"],
        output_names = ["value"]
        ).from_apply_func(
                custom_indicator,
                window = 14
                )

res = ind.run(btc_price, window = 21)

print(res.value)

entries = res.value == 1.0
exits = res. value == -1.0

pf = vbt.Portfolio.from_signals(btc_price, entries, exits)
print(pf.stats())
