Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s=input()
alphabet=list()
sum=0
for x in s:
  if x>='0' and x<='9':
    sum+=int(x)
  else:
    alphabet.append(x)
alphabet.sort()

res=""
for x in alphabet:
  res+=x
res+=str(sum)
print(res)