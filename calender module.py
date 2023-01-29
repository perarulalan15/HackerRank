#import calendar
import datetime 
date=str(input('Enter the date:'))
day_name= ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
day = datetime.datetime.strptime(date, '%m %d %Y').weekday()
result=(day_name[day])
print(result.upper()) 