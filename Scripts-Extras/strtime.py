import datetime

took = '2020-01-01 ' + '08:15:27.243860'

took2 = "2020-01-01 00:00:00.0049698"

print (took)
print (took2)

#date_time_str = '2018-06-29 08:15:27.243860'
date_time_obj = datetime.datetime.strptime(took, '%Y-%m-%d %H:%M:%S.%f')

print('Date:', date_time_obj.date())
print('Time:', date_time_obj.time())
print('Date-time:', date_time_obj)