import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import time 
from openpyxl.workbook import Workbook

api_key = '281HZI70O9LVNK4L'

my_symbol = input('Type your stock name ')
#This line to put the symbol and timefram

ts = TimeSeries(key=api_key , output_format='pandas')
data , meta_data = ts.get_intraday(symbol = my_symbol , interval = '1min', outputsize = 'full')
print (data)

#This Line for get the data evry 60sec

i = 1
#while i==1:
	#data , meta_data = ts.get_intraday(symbol = 'USD' , interval = '1min', outputsize = 'full')
	#data.to_excel('stock.xlsx')
	#time.sleep(60)


#This line for claculate the change on (%) for the closing price

close_data = data['4. close']
percentage_change = close_data.pct_change()

print(percentage_change)

#to get last change

last_change = percentage_change[-1]

#if absaloute value is above (i) percentage = to some action 
#we can creat whatsup or email notefication

if abs(last_change) > 0.0004 :
	print(f"{my_symbol} Alert:" + str(last_change))