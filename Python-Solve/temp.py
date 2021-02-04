import csv

f = open("D:/기상자료개방포털.csv")
data = csv.reader(f)

test = []
for row in data:
    test.append(row)
    
max = 0
for row in (test[8:]):
    if(row[4]):
        if max < float(row[4]):
            max = float(row[4])
            
print(max)