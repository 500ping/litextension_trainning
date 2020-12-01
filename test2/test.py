from datetime import datetime
# 10/1/2019 13:32
# datetime_str = '09/19/18 13:55:26'
datetime_str = '10/1/2019 13:32:00'

datetime_object = datetime.strptime(datetime_str, '%m/%d/%Y %H:%M:%S')

print(type(datetime_object))
print(datetime_object)  # printed in default format