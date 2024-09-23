import vectorbt as vbt
import pandas as pd
import numpy as np
import datetime

end = datetime.datetime.now()
start = end - datetime.timedelta(days=3)

vbt.settings.set_theme("dark")
vbt.settings["plotting"]["layout"]["width"] = 1200
vbt.settings["plotting"]["layout"]["height"] = 600

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

fig = btc_price.vbt.plot(trace_kwargs=dict(name='Price', line=dict(color='red')))
fig = fast_ma.ma.vbt.plot(trace_kwargs=dict(name='Fast_ma', line=dict(color='blue')), fig=fig)
fig = slow_ma.ma.vbt.plot(trace_kwargs=dict(name='Slow_ma', line=dict(color='green')), fig=fig)
fig = entries.vbt.signals.plot_as_entry_markers(btc_price, fig=fig)
fig = exits.vbt.signals.plot_as_exit_markers(btc_price, fig=fig)

fig.show()

