
f = open('C:/Users/user/Desktop/github/Python/새파일.txt','a')
for i in range(11, 20):
    data = "%d 번째 줄입니다.\n" % i
    f.write(data)
f.close()