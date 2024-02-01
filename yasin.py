import datetime

import os

import time

now = datetime.datetime.now()

alarm_time = datetime.datetime.combine(now.date(), datetime.time(13,30,0))

time.sleep((alarm_time - now).total_seconds())

os.system("start Alone")