Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> n=int(input())
coin=list(map(int,input().split()))
coin.sort()
target=1
for x in coin:
  if target<x:
      break
  target+=x
print(target)