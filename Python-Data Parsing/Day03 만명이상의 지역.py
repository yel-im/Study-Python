import csv

f = open("C:/Users/user/Desktop/github/Python/자료/연령별인구현황_월간.csv")
data = csv.reader(f)

rawData = []
for row in data:
    rawData.append(row)
    
total = []
for idx , row in enumerate(rawData[1:]):
    a = row[1].replace(',','')
    if int(a) > 10000:
        total.append(row)
