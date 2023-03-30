n= int(input())
trips=input().split()
dx=[1,-1,0,0]
dy=[0,0,1,-1]
direct=['R','L','D','U']

x_start=1
y_start=1

nx,ny=1,1

for trip in trips:
    idx=direct.index(trip)
    if x_start+dx[idx]>=1 and x_start+dx[idx]<=n and y_start+dy[idx]>=1 and y_start+dy[idx]<=n:
        nx+=dx[idx]
        ny+=dy[idx]

print(nx,ny)