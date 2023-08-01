import datetime

# 假设你的时间戳为 timecreated
timecreated = 1690891780

# 将时间戳转换为日期时间
datetime_obj = datetime.datetime.fromtimestamp(timecreated)

# 输出结果
print(datetime_obj)