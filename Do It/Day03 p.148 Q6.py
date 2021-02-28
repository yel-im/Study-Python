numbers = [1, 2, 3, 4, 5]

result = []
for n in numbers:
    if n % 2 ==1:
        result.append(n*2)
        
numbers = [1, 2, 3, 4, 5]
result = [a*2 for a in numbers if a%2 == 1]
#가장 일반적인 리스트 내포임::for문- if문- 앞으로 돌아와서 a*2 순서