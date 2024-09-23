import pandas as pd
import vectorbt as vbt
import numpy as np
import datetime
import talib

now = datetime.datetime.now()
before = now - datetime.timedelta(days=3)

btc_price = vbt.YFData.download(
        "BTC-USD",
        missing_index="drop",
        interval="1m",
        start=before.timestamp(),
        end= now.timestamp()).get("Close")

btc_price, range_indexes = btc_price.vbt.range_split(n=100, range_len=1440)

def optimize_rsi(close, window, entry, exit):
    rsi = vbt.IndicatorFactory.from_talib("RSI").run(close, timeperiod=window).real
    return rsi < entry, rsi > exit

rsi_ind = vbt.IndicatorFactory(
        class_name="optimzeRSI",
        short_name="rsi",
        input_names=["close"],
        param_names=["window", "entry", "exit"],
        output_names=["entries", "exits"]
        ).from_apply_func(
                optimize_rsi,
                window=14,
                entry=30,
                exit=70
                )
        

step_size = 2
entries = np.arange(10, 45, step=step_size, dtype= int)
exits  = np.arange(55, 95, step=step_size, dtype= int)
windows  = np.arange(10, 45, step=step_size, dtype= int)

rsi_res = rsi_ind.run(
        btc_price,
        window=windows,
        entry=entries,
        exit=exits,
        param_product=True
        )

rsi_entries = rsi_res.entries
rsi_exits = rsi_res.exits

rsi_exits.iloc[-1, :] = True

rsi_pf = vbt.Portfolio.from_signals(btc_price, rsi_entries, rsi_exits, freq="1T", fees=0.001)

rsi_tot_returns = rsi_pf.total_return().groupby(
        level = ['rsi_exit', 'rsi_entry']).mean()

print(rsi_tot_returns)

fig = rsi_pf.total_return().vbt.heatmap(
        x_level="rsi_exit",
        y_level="rsi_entry",
        )

fig.show()


