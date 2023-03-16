start = input()
tmp_x=start[0] 
start_y=int(start[1]) # y 시작좌표

x=['a','b','c','d','e','f','g','h']
start_x=x.index(tmp_x)+1 # x 시작 좌표

steps=[(2,1),(2,-1),(-2,1),(-2,-1),(1,-2),(-1,-2),(1,2),(-1,2)] #갈수 있는 모든 방향

count = 0
for x,y in steps:
    move_x=start_x+x
    move_y=start_y+y
    if move_x<1 or move_x>8 or move_y<1 or move_y>8:
        pass
    else:
        count+=1
    
print(count)
        
