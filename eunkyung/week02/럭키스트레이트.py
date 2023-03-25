n=list(input()) # 파이썬은 입력받은 데이터가 문자열 형태
length=len(n)
mid=length//2

front=0
back=0

for i in range(mid): # 0 ~ 절반
    front+=int(n[i])

for i in range(mid,length): # 절반 ~ 끝
    back+=int(n[i])

if front==back:
    print('LUCKY')
else:
    print('READY')

