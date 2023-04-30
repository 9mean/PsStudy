def binary_search(x,arr):
    global cnt
    start,end=0,n-1
    
    while start<=end:
        mid=(start+end)//2
        
        if arr[mid]==x:
            cnt+=1
            #왼쪽으로 오른쪽으로 x가 있는지 탐색하기
            searchLeft(x,arr,mid)
            searchRight(x,arr,mid)
            return
        if arr[mid]>x:
            end=mid-1
        else:
            start=mid+1
            
def searchLeft(x,arr,idx):
    global cnt
    for i in range(idx-1,-1,-1):
        if arr[i]==x:
            cnt+=1
        else:
            return
def searchRight(x,arr,idx):
    global cnt
    for i in range(idx+1,n-1):
        if arr[i]==x:
            cnt+=1
        else:
            return
n,x=map(int,input().split())
arr=list(map(int,input().split()))
cnt=0

binary_search(x,arr)
if cnt==0:
    cnt=-1
print(cnt)
