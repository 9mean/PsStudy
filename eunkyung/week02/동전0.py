# 백준 11047번 -- 그리디

n,k=map(int,input().split()) # n: 총 동전 종류 개수 , k: 만들려고 하는 동전의 합

#모든 금액은 다 배수 관계이다. 
#큰수들은 작은 수들의 배수로 만들수 있기때문에 최대한 큰수부터 사용해야 동전을 최소로 사용할수 있다.

coins=[] # 동전 종류를 저장할 배열
for _ in range(n): # 동전 종류 저장
    x=int(input())
    coins.append(x)

coins.reverse() # 내림차순으로 배열 저장 (arr.reverse() 리스트값 반대로 뒤집는 함수)
coins
result=0

for coin in coins:
    result+=k//coin
    k=k%coin

print(result)





