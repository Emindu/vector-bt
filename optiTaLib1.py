import vectorbt as vbt
import pandas as pd
import numpy as np
import datetime
import talib

end = datetime.datetime.now()
start = end - datetime.timedelta(days=7)

btc_price = pd.read_csv("data.csv")
btc_price["Datetime"] = pd.to_datetime(btc_price["Datetime"])
btc_price.set_index("Datetime", inplace=True)

print(btc_price)

RSI = vbt.IndicatorFactory.from_talib('RSI')

def produce_signal(rsi, entry, exit):
    trend = np.where((rsi > exit) , -1, 0)
    trend = np.where((rsi < entry), 1 , trend)
    return trend

#This is custom indicator funtion
def custom_indicator(close, rsi_window = 14, entry = 30, exit = 70):
    rsi  =  RSI.run(close, rsi_window).real 
    return produce_signal(rsi, entry, exit)

#Indicator factory
ind = vbt.IndicatorFactory(
        class_name = "Combination",
        short_name = "comb",
        input_names = ["close"],
        param_names = ["rsi_window", "entry", "exit"],
        output_names = ["value"]
        ).from_apply_func(
                custom_indicator,
                rsi_window = 14,
                entry = 30,
                exit = 70,
                to_2d=False 
                )

res = ind.run(
        btc_price, 
        rsi_window = np.arange(10,40,step=3, dtype=int),
        #ma_window = np.arange(20,200,step=20, dtype=int),
        entry = np.arange(10,40,step=2, dtype=int),
        exit = np.arange(60,85,step=2, dtype=int),
        param_product = True
        )

print(res.value)

entries = res.value == 1.0
exits = res. value == -1.0

pf = vbt.Portfolio.from_signals(btc_price, entries, exits)
returns = pf.total_return()

#selecting one symbol
#returns = returns[returns.index.isin(["BTC-USD"], level="symbol")]


#returns = returns.groupby(level=["comb_exit", "comb_entry", "symbol"]).mean()

print(returns.to_string())

print(returns.max())
print(returns.idxmax())



#comb_rsi_window  comb_ma_window

#fig = returns.vbt.volume(
#        x_level = "comb_exit",
#        y_level = "comb_entry",
#        z_level = "comb_rsi_window",
#        slider_level = "symbol",
#        )
#fig.show()
