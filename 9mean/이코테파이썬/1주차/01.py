#큰수의 법칙
n, m, k = map(int, input().split())
index = list(map(int, input().split()))

index.sort(reverse=True)
a = index[0]
b = index[1]

#sum = 0
sum = (m // (k + 1)) * (k * a + b) + (m % (k + 1)) * a
print(sum)
