n=input()
alpha=[]
num=0
for s in n:
    if s.isalpha(): # 알파벳인지 확인
        alpha.append(ord(s))
    if s.isdigit(): # 숫자이면 or else 사용
        num+=int(s)

alpha.sort() # 알파벳 오름차순 정렬

result=''

for x in alpha:
    result+=chr(x)

result+=str(num)

print(result)

