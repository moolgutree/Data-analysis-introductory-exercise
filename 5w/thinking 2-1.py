import csv

f = open('subwaytime.csv')
data = csv.reader(f)
header = next(data)
header = next(data)

mx=0
low=0
mxs=''
lows=''
repo=[]
lowRepo=[]

for row in data:
    for i in range(10, 12):
        row[i] = int(row[i].replace(',',''))
    if row[10] > mx:
        mx = row[10]
        repo = row[10]
        mxs = row[1]+ ' ' + row[3]
    if row[11] > low and row[11] > 1:
        low = row[11]
        lowRepo = row[11]
        lows = row[1] + ' ' + row[3]
        
print(mxs, round(repo,2))
print(lows, round(lowRepo,2))

f.close()
