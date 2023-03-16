#숫자카드게임
n, m = map(int, input().split())
all_min = []
for i in range(n):
  a = list(map(int, input().split()))
  all_min.append(min(a))

print(max(all_min))
