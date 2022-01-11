from collections import defaultdict

def formattime(time):
    iptime = time.split('.')
    print iptime
    return iptime[0] + ':' + str(int(float(iptime[-1])/1000))

ip = open('timeserieshcidata.txt')

readings = ip.readlines()

ddict = defaultdict(float)
cdict = defaultdict(float)

dlist = []
clist = []

for r in readings:
    data = r.strip().split(',')
    time = formattime(data[2])
    ddict[time] = float(data[3])
    cdict[time] = float(data[7])
    break
print ddict, cdict