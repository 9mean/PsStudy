#곱하기 혹은 더하기
a = input()
out = int(a[0])
for i in range(1, len(a)):
  n = int(a[i])
  if n <= 1 or out <= 1:
    out += n
  else:
    out *= n

print(out)
