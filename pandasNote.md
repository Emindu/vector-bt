




# Pandas axis vs broadcast_axis



1.	Purpose:
	•	axis: Specifies along which dimension (rows or columns) the alignment should be done.
	•	broadcast_axis: Specifies the direction in which to broadcast values to match the shape of the other DataFrame (or Series).
	2.	Effect:
	•	axis: Aligns the DataFrames along the specified dimension, ensuring they have the same labels along that dimension.
	•	broadcast_axis: Repeats values along the specified dimension to match the shape of the other DataFrame (or Series).
	3.	Usage Context:
	•	Use axis when you need to ensure that both DataFrames have the same labels along a particular dimension.
	•	Use broadcast_axis when you need to repeat values along a particular dimension to make the DataFrames align correctly.



# Loading price data to csv using Bitstamp

- src: https://greyhoundanalytics.com/blog/get-historical-crypto-price-data-from-bitstamp-in-python/
- getOHLCData.py

