f = open('C:/Users/user/Desktop/github/Python/새파일.txt', 'r')
body = f.read()
f.close()

body = body.replace('java','python')

f = open ('C:/Users/user/Desktop/github/Python/새파일.txt','w')
f.write(body)
f.close()