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


fig = pf.plot(subplots = [
    ('price', dict(
        title='Price',
        yaxis_kwargs=dict(title='Price')
        )), 
    ('price', dict(
        title='Price',
        yaxis_kwargs=dict(title='Price')
        )), 
    'orders',
    'trade_pnl',
    'cum_returns',
    'drawdowns'],
    make_subplots_kwargs=dict(rows=10, cols=2))

#adding custom plot to position 1,1
scatter = vbt.plotting.Scatter(
        data = btc_price,
        x_labels = btc_price.index,
        trace_names = ["Price"],
        trace_kwargs=dict(line=dict(color='red')),
        add_trace_kwargs=dict(row=1, col=1),
        fig=fig
        )

#adding custom plot to position 2,1
fast_ma_scatter  = vbt.plotting.Scatter(
        data = fast_ma.ma,  
        x_labels = fast_ma.ma.index,
        trace_names = ["Fast_MA"],
        trace_kwargs=dict(line=dict(color='green')),
        add_trace_kwargs=dict(row=2, col=1),
        fig=fig
        )


#adding custom plot to position 3,1
slow_ma_scatter  = vbt.plotting.Scatter(
        data = slow_ma.ma,  
        x_labels = slow_ma.ma.index,
        trace_names = ["Slow_MA"],
        trace_kwargs=dict(line=dict(color='blue')),
        add_trace_kwargs=dict(row=2, col=1),
        fig=fig
        )

entries_plot = entries.vbt.signals.plot_as_entry_markers(
        slow_ma.ma,
        add_trace_kwargs=dict(row=2,col=1),
        fig=fig
        )

exits_plot = exits.vbt.signals.plot_as_exit_markers(
        slow_ma.ma,
        add_trace_kwargs=dict(row=2,col=1),
        fig=fig
        )

#adding horizontal line in map
fig.add_hline (
        y = 58000,
        line_color= '#FFFFFF',
        row=2,
        col = 1,
        line_width=20
        )

#fig = btc_price.vbt.plot(trace_kwargs=dict(name='Price', line=dict(color='red')))
#fig = fast_ma.ma.vbt.plot(trace_kwargs=dict(name='Fast_ma', line=dict(color='blue')), fig=fig)
#fig = slow_ma.ma.vbt.plot(trace_kwargs=dict(name='Slow_ma', line=dict(color='green')), fig=fig)
#fig = entries.vbt.signals.plot_as_entry_markers(btc_price, fig=fig)
#fig = exits.vbt.signals.plot_as_exit_markers(btc_price, fig=fig)

fig.show()

