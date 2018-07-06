import time

unix_time = int(time.time())
print(unix_time)

struct_time = time.localtime()
print(struct_time)

time_now = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
#strftime(struct_time， strin_format) 将指定的struct_time根据格式化字符串输出
print("当前标准时间 %s" % time_now)

#time.mktime(struct_time)  struct_time转换为unix时间
unx_time = time.mktime(time.localtime())
print(unx_time)

time_cost = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(unix_time + 5866))
print(time_cost)
