import vectorbt as vbt
import pandas as pd
import numpy as np
import datetime

end = datetime.datetime.now()
start = end - datetime.timedelta(days=3)

btc_price = vbt.YFData.download(
	["BTC-USD"],
	missing_index='drop',
	start= start,
	end=end,
	interval="1m"
	).get("Close")

print(btc_price)

fast_ma = vbt.MA.run(btc_price, window =50)
slow_ma = vbt.MA.run(btc_price, window = 200)

entries = fast_ma.ma_crossed_above(slow_ma)
exits = fast_ma.ma_crossed_below(slow_ma)

pf = vbt.Portfolio.from_signals(btc_price, entries, exits)

#pf.plot().show()
#pf.trades.plot_pnl().show()
pf.trades.plot().show()


