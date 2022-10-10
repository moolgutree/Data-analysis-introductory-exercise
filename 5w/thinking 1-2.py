#유무임 승하차 인원이 가장 많은 역

import csv

f = open('subwayfee.csv', encoding='UTF-8')
data = csv.reader(f)
header = next(data)

A=0
B = input("알고싶은 유무임 승하차를 입력하세요 ex)유임승차 = 1, 유임하차 = 2, 무임승차 = 3, 무임하차 = 4 >>>")

mx=0
rate=0
mxs=''
repo=[]
if B == '1':
    A = int(4)
elif B == '2':
    A = int(5)
elif B == '3':
    A = int(6)
elif B == '4':
    A = int(7)
else:
    print("다시 입력하세요")

for row in data:
    for i in range(4, 8):
        row[i] = int(row[i].replace(',',''))
    if row[A] > mx:
        mx = row[A]
        repo = row[A]
        mxs = row[1]+ ' ' + row[3]
print(mxs, round(repo,2))

f.close()
