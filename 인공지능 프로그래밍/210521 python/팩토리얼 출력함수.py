n=int(input('팩토리얼을 구하고 싶은 값을 입력하세요 \n'))
def fac(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f
print(fac(n))
