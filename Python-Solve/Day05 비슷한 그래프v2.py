import csv
import matplotlib.pyplot as plt

f = open('C:/Users/user/Desktop/github/Python/Study-Python/Python-Solve/자료/연령별인구현황_월간.csv')
data = csv.reader(f)

rawData = []
result = []
#result[] = 신도림동의 각 나이별 인구 수

for row in data:
    rawData.append(row)
    
for idx, row in enumerate(rawData[:]):
    if '신도림' in row[0]:
        for age in row[3:103]:
            result.append(int(age.replace(',','')))

result2 = []
min = 999999
for idx2, row2 in enumerate(rawData[1:]):
    
    if '신도림' not in 
    
    row2[0]:
        
        for idx3, row3 in enumerate(row2[3:103]):
            result2.append(abs(result[idx3]/result[1] - (int(row2[1].replace(',',''))/int(row3.replace(',','')))))
        
        temp=sum(result2)
        
        if temp < min:
            min = temp
            area = idx2
        
        result2 = []
        
    
print(rawData[area+1][0])


        
plt.plot(result)

