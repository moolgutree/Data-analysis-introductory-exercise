#시간대별로 사람들이 가장 많이 타고 내리는 역

import csv

f = open('subwaytime.csv')
data = csv.reader(f)
header = next(data)
header = next(data)

mx=int(0)
low=int(0)
mxs=''
lows=''
repo=[]
lowRepo=[]


for row in data:
    for i in range(4, 50):
        row[i] = int(row[i].replace(',',''))
    for j in range(24):
        A = int(row[2 * j + 4])
        if A > mx:
            mx = A
            repo = A
            rideTime= j + 4
            mxs = row[1]+ ' ' + row[3]
    for y in range(24):
        B = int(row[2 * y + 5])
        if B > low:
            low = B
            lowRepo = B
            letDownTime = y + 4
            lows = row[1] + ' ' + row[3]
        
print(mxs, round(repo,2), rideTime, '시')
print(lows, round(lowRepo,2), letDownTime, '시')

f.close()
