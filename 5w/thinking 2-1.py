import csv

f = open('subwayfee.csv', encoding='UTF-8')
data = csv.reader(f)
header = next(data)

mx=0
rate=0
mxs=''
repo=[]
for row in data:
    for i in range(4, 8):
        row[i] = int(row[i].replace(',',''))
    if row[4] > mx:
        mx = row[4]
        repo = row[4]
        mxs = row[1]+ ' ' + row[3]
print(mxs, round(repo,2))

f.close()
