import csv
#import matplotlib.pyplot as plt

f = open("C:/Users/user/Desktop/github/Python/자료/연령별인구현황_월간.csv")
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
    if '신도림' not in row2[0]:
    #신도림동이 아닌 행정구역을 만나면
        
        for idx3, row3 in enumerate(row2[3:103]):
        #그 지역의 index 3의 data(0세 인구수)부터 index 103을
            result2.append(abs(result[idx3] - (int(row3.replace(',','')))))
            #신도림동의 idx3번째 인구수와 row3의 인구수를 뺀 뒤 절댓값을 씌움
            #절댓값이 씌워진 값을 result2에 추가
            #abs : 절댓값으로 만듦, replace : 첫번째 ''를 빼고 두 번째''를 넣음
        
        temp=sum(result2)
        #temp = 신도림동의 각 인구수를 row2지역의 각 인구수를 뺀 수가 담긴 result2[]를 모두 더한 값
        
        if temp < min:
            min = temp
            area = idx2
            #row2의 for문이 돌아갈 때 마다 행정구역이 바뀜
        
        result2 = []
        #다시 새로운 행정구역의 인구와 for문을 돌아야 하기 때문에 result2를 비워줌
    
print(rawData[area+1][0])


        
#plt.plot(result)

