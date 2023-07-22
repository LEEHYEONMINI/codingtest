str = input()
r = "" # r이라는 비어있는 문자열 변수 생성
for i in str:
    if i.islower(): # i의 값이 소문자면
        r += i.upper()
    else:
        r += i.lower()
print(r)