def binarySearch(start,end,arr):
    
    while start<=end:
        mid=(start+end)//2
        #고정점 찾으면 출력
        if arr[mid]==mid:
            return mid
        #배열이 오름차순으로 정렬되어있으므로 arr[mid]의 값이 mid보다 크면 고정점은 왼쪽에 있는거임
        elif arr[mid]>mid:
            end=mid-1
        else:
            start=mid+1
    return -1

n=int(input())
arr=list(map(int,input().split()))
print(binarySearch(0,n-1,arr))


