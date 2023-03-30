# 1원부터 모든 돈의 합까지의 금액을 만들수 있는지 확인
# 모든 경우의 수를 다 따져서 해당 금액을 만들수 있는지 확인후 만들수 없으면 그 수가 답

n = int(input())
coins =list(map(int,input().split()))
coins.sort() # 오름차순
# 모든 경우의 수는 어떻게 확인할건지
# 동전이 총 n 개라고 하면 1개로 만들수 있는 모든 경우의수, 2개로 만들수 있는 모든 경우의수, ... (n-1) 개로 만들수 있는 경우의수

values=[x for x in range(1,sum(coins))] # 1부터 모든 금액을 합한 금액까지 

for i in range(1,sum(coins)-1):
    



