
import vectorbt as vbt
import datetime

end_date = datetime.datetime.now()
start_date = end_date - datetime.timedelta(days = 3 )

btc_price = vbt.YFData.download(
            ["BTC-USD", "ETH-USD", "XMR-USD", "ADA-USD"],interval="1m",
	    start = start_date,
	    end = end_date,  missing_index='drop').get('Close')


print(btc_price)

rsi = vbt.RSI.run(btc_price,window= [14, 21])
print(rsi.rsi)


# In vector bt entries and exiting are denine as boolean values
entries = rsi.rsi_crossed_below(30) 
exits = rsi.rsi_crossed_above(70)

print(entries.to_string())
print(exits.to_string())


pf = vbt.Portfolio.from_signals(btc_price, entries, exits)

print(pf.total_return())

#pf.plot().show()
