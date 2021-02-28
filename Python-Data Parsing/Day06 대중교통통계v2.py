import csv

f = open("C:/Users/user/Desktop/github/Python/자료/subway_data.CSV")
data = csv.reader(f)

rawData = []
for row in data:
    rawData.append(row)

total = [0]*48
area = []


for idx,row in enumerate(rawData[2:]):
    result = []
    for idx2, row2 in enumerate(row[4:52]):
        result.append(int(row2.replace(',','')))
    for idx3, row3, in enumerate(result):
        if total[idx3] < row3:
            total[idx3] = row3
            area = idx