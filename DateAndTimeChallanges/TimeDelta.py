import datetime

def time_delta(t1, t2):
    timeFormat = "%a %d %b %Y %H:%M:%S %z"
    time1 = datetime.datetime.strptime(t1,timeFormat)
    time2 = datetime.datetime.strptime(t2,timeFormat)
    result = (time2-time1).total_seconds()
    return int(abs(result))

t = int(input().strip())
for a0 in range(t):
    t1 = input().strip()
    t2 = input().strip()
    delta = time_delta(t1, t2)
    print(delta)
