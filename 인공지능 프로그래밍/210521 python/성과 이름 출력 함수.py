def div_name(name):
    return name[0],name[1:len(name)]
# 이름이 3글자라고 가정하고 첫 글자를 성으로 인식하는 함수
def div_name2(name):
    return name[0], name[1] + name[2]

print(div_name("홍길동"))
print(div_name("또치"))
