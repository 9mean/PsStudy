#모험가길드
n = int(input())
r = list(map(int, input().split()))
count = 0
group = 0
r.sort()

for i in r:
  count += 1
  if count >= i:
    r += 1
    count = 0

print(r)
