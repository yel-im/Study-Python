import csv

f = open("C:/Users/user/Desktop/github/Python/자료/subway_data.CSV")
data = csv.reader(f)

rawData=[]
maxOn = 0
maxOff = 0
for row in data:
    rawData.append(row)

for idx,row in enumerate(rawData[2:]):
    temp = 0
    temp2 = 0
    for idx2, row2 in enumerate(row[4:52]):
        if idx2%2 == 0:
            temp = temp + int(row2.replace(',',''))
        if idx2%2 == 1:
            temp2 = temp2 + int(row2.replace(',',''))
            
    if maxOn < temp:
        maxOn = temp
        final_flag = idx
        
    if maxOff < temp2:
        maxOff = temp2
        final_flag2 = idx
        
print('승차 인원이 가장 많은 역은 '+rawData[final_flag+2][3]+'역 입니다')
print('하차 인원이 가장 많은 역은 '+rawData[final_flag2+2][3]+'역 입니다')