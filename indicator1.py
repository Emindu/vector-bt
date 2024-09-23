import vectorbt as vbt
import pandas as pd
import numpy as np
import datetime

end = datetime.datetime.now()
start = end - datetime.timedelta(days=2)

btc_price = vbt.YFData.download(
	"BTC-USD",
	missing_index='drop',
	start= start,
	end=end,
	interval="1m"
	).get("Close")

#This is custom indicator funtion
def custom_indicator(close, window = 14):
    rsi = vbt.RSI.run(close, window = window)
    return rsi.rsi

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

