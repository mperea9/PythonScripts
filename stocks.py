import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import time 

api_key = 'JB16JCLP8ZBBPJTU'			# our API Key

ts = TimeSeries(key = api_key, output_format = 'pandas')  # output format as pandas data frame
data, meta_data = ts.get_intraday(symbol = 'MSFT', interval = '1min', outputsize = 'full')	# minute by minute data, using microsoft ticker
print(data)

close_data = data['4. close']					# closing data of he stock in each minute, using the closing column 4 in pandas data frame
percentage_change = close_data.pct_change()		# we get percentage change inbetween each minute in closing data
print(percentage_change)

last_change = percentage_change[-1]				# grabs the last change from the pandas data frame

if abs(last_change) > .0004:					# create a tolerance so if stock changes by .0004 we get an alert
	print("MSFT Alert: " + str(last_change))