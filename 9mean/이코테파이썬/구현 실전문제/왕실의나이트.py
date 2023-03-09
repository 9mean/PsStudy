Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> k=input()
alphabet=['a','b','c','d','e','f','g','h']
dx=[-1,1,2,-2]
x,y=0,int(k[1])
cnt=0
for i in range(8):
  if k[0]==alphabet[i]:
    x=i+1
    break
for i in dx:
  if i==-1:
    if x-1>0:
      if y+2<9:
        cnt+=1
      if y-2>0:
        cnt+=1
  if i==1:
    if x+1<9:
      if y+2<9:
        cnt+=1
      if y-2>0:
        cnt+=1
  if i==2:
    if x+2<9:
      if y+1<9:
        cnt+=1
      if y-1>0:
        cnt+=1
  if i==-2:
    if x-2>0:
      if y+1<9:
        cnt+=1
      if y-1>0:
        cnt+=1
print(cnt)