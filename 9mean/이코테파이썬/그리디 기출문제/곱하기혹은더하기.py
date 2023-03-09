Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s=input()
res=0
how='+'
length=len(s)
for i in range(length):
  #현재 res나 현재 값이 0이나 1이면 뒤에 값이랑은 +를 하자 
  if s[i]=='0' or s[i]=='1' or res==0 or res==1:
    how='+'
    #연산이 더하기면 res에 더하고 곱하기로 연산 초기화
  if how=='+':
    res+=int(s[i])
    how='*'
    #곱하기면 곱하기  
  else:
    res*=int(s[i])
print(res)
