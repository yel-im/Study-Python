import csv

f = open('C:/Users/user/Desktop/github/Python/Study-Python/Python-Solve/자료/연령별인구현황_월간.csv')
data = csv.reader(f)

rawData = []
for row in data:
    rawData.append(row)
    
for idx , row in enumerate(rawData[:]):
        if '신도림동' in row[0]:
            print(idx)