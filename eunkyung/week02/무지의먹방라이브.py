def solution(food_times, k):
    answer = 0
    while True:
        if k==0:
            break
        for idx in range(len(food_times)):
            if food_times[idx]>0:
                food_times[idx]=food_times[idx]-1
                k-=1
                answer=idx+1
            if sum(food_times)==0:
                return -1
    return answer

print(solution([3,1,2],5))