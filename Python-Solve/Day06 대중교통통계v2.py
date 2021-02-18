import csv

f = open('D:자료/subway_data.CSV')
data = csv.reader(f)

rawData = []
maxOn = 0
maxOff = 0
totalOn = []
totalOff = []

for row in data:
    rawData.append(row)

for idx,row in enumerate(rawData[2:]):
    temp = []
    temp2 = []
    for idx2, row2 in enumerate(row[4:52]):
        if idx2%2 == 0:
            temp.append(row2.replace(',',''))
        if idx2%2 == 1:
            temp2.append(row2.replace(',',''))
    totalOn.append(temp)
    totalOff.append(temp2)

#시간별 승차인원을 temp에 넣고 지하철역 별로 구해 totalOn에 넣음 (하차는 totalOff)