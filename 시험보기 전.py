import csv
import matplotlib.pyplot as plt

f = open('seoul_0914.csv')
data = csv.reader(f)

header=next(data);
# header가 2개면 2개 쓰면 됨

result = []
for row in data:
    if row[4] != '':
        row[4] = float(row[4])      # float 실수 , int 정수.
        result.append(float(row[4]))

plt.rc('font', family='Malgun Gothic')  #한국어 사용
plt.rcParams['axes.unicode_minus'] = False  #음수코드 사용(한국어중에서도)  / rc,rcParams는 그래프 그리기 전에(plt.figute 전에) 사용해야 함
plt.figure()  # 흰색 도화지
plt.plot(result, label='abc')  # 선 그래프 그리기 , 레이블 딱지 붙이기
plt.title('안녕하세요') 
plt.xlabel('연도')
plt.ylabel('Temperture')
plt.grid(True)  #격자
plt.show() # 나한테 보여줘라
