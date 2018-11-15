import re
from datetime import datetime, timezone, timedelta

def to_timestamp(dt_str, tz_str):
    retest = re.split('[C:]',tz_str)
    tz_utc = timezone(timedelta(hours=int(retest[1])))
    dt = list(map(int,re.split('[- :]',dt_str)))
    
    res = datetime(dt[0], dt[1], dt[2], dt[3], dt[4], dt[5], tzinfo=tz_utc)
    re_tz = datetime.timestamp(res)
    return re_tz


# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')