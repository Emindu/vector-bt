import vectorbt as vbt
import pandas as pd
import numpy as np
import datetime

end = datetime.datetime.now()
start = end - datetime.timedelta(days=7)

btc_price = vbt.YFData.download(
	["BTC-USD", "ETH-USD"],
	missing_index='drop',
	start= start,
	end=end,
	interval="1m"
	).get("Close")

#This is custom indicator funtion
def custom_indicator(close, rsi_window = 14, ma_window = 50, entry = 30, exit = 70):
    close_5m = close.resample("5T").last()
    rsi_5m = vbt.RSI.run(close_5m, window = ma_window).rsi
    print(rsi_5m)
    #we need to down sample 5min rsi to 1m to
    rsi, _ = rsi_5m.align(close,
                       broadcast_axis=0, method='ffill', join='right')

    close = close.to_numpy()
    rsi = rsi.to_numpy()
    
    ma = vbt.MA.run(close, window = ma_window).ma
    ma = ma.to_numpy()

    trend = np.where((rsi > exit) & (close > ma), -1, 0)
    trend = np.where((rsi < entry) & (close < ma), 1 , trend)
    print("printing trend values")
    print(trend)
    return trend

#Indicator factory
ind = vbt.IndicatorFactory(
        class_name = "Combination",
        short_name = "comb",
        input_names = ["close"],
        param_names = ["rsi_window", "ma_window", "entry", "exit"],
        output_names = ["value"]
        ).from_apply_func(
                custom_indicator,
                rsi_window = 14,
                ma_window = 50,
                entry = 30,
                exit = 70,
                keep_pd=True
                )

res = ind.run(
        btc_price, 
        rsi_window = np.arange(10,40,step=3, dtype=int),
        ma_window = np.arange(20,200,step=20, dtype=int),
        entry = np.arange(10,40,step=4, dtype=int),
        exit = np.arange(60,85,step=4, dtype=int),
        param_product = True
        )

print(res.value)

entries = res.value == 1.0
exits = res. value == -1.0

pf = vbt.Portfolio.from_signals(btc_price, entries, exits)
returns = pf.total_return()

#selecting one symbol
#returns = returns[returns.index.isin(["BTC-USD"], level="symbol")]


returns = returns.groupby(level=["comb_exit", "comb_entry", "symbol"]).mean()

print(returns.to_string())

print(returns.max())
print(returns.idxmax())



#comb_rsi_window  comb_ma_window

fig = returns.vbt.heatmap(
        x_level = "comb_exit",
        y_level = "comb_entry",
        slider_level = "symbol",
        )
fig.show()
