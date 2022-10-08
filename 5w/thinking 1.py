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
    rate = row[4]/(row[4]+row[6])
    if rate > mx and rate != 1:
        mx=rate
        repo = rate
        mxs = row[1]+ ' ' + row[3]
print(mxs, round(repo,2))

f.close()
