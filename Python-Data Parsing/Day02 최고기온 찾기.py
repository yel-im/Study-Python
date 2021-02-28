import csv

f = open("C:/Users/user/Desktop/github/Python/자료/기상자료개방포털.csv")
data = csv.reader(f)

test = []
for row in data:
    test.append(row)
    
max = 0
#enumerate는 for문이 몇 번째 반복되는지 index변수에 담아준다
for idx, row in enumerate(test[8:]):
    if(row[4]):
        if max < float(row[4]):
            max = float(row[4])
            date = idx
            
print(test[date+8][0],max)