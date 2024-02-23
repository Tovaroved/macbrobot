from datetime import datetime, timedelta
import gspread

#start_time_str = input('time up: ')
#end_time_str = input('time down: ')

#start_time = datetime.strptime(start_time_str, "%H:%M")
#end_time = datetime.strptime(end_time_str, "%H:%M")

#duration = end_time - start_time

#print(f"{duration}")



sa = gspread.service_account()  
sh = sa.open("MacPython")
wks = sh.worksheet('Получение посылок - 24')
#print(wks.get("A1:E36"))
#print(len(wks.get("A1:E36")))
worksheet_list = sh.worksheets()
print(worksheet_list)

