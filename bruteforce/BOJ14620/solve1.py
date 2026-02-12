import sys

def input():
    return sys.stdin.readline().rstrip()
#상하좌우
direc = [(1,0),(-1,0),(0,-1),(0,1)]

def dfs(idx,count,total_cost):
    #종료조건
    if count==3:
        return total_cost
    min_cost = float('inf')
    
    for k in range(idx,len(board_price)):
        i,j,price = board_price[k]

        #꽃 배치가 가능한가?
        if can_place(i,j):
            #이제 배치를 한다.
            place_flower(i,j)
            #다음 꽃 선택을 해야 한다.
            result = dfs(k+1,count+1,total_cost+price)
            min_cost = min(min_cost,result)
            remove_flower(i,j)

    return min_cost

def remove_flower(i,j):
    visited[i][j] = False

    for di,dj in direc:
        ni,nj = i+di,j+dj
        visited[ni][nj] = False
        
    
def place_flower(i,j):
    visited[i][j] = True

    for di,dj in direc:
        ni,nj = i+di,j+dj
        visited[ni][nj] = True


def can_place(i,j):
    if visited[i][j]:
        return False
    for di,dj in direc:
        ni,nj = i+di,j+dj
        if visited[ni][nj]:
            return False
    return True

N = int(input())
board = []
visited = [[False]*N for _ in range(N)]
board_price = []
for _ in range(N):
    line = list(map(int,input().split()))
    board.append(line)

#board를 돌면서 각 지점에 꽃을 심을 경우 발생하는 가격을 저장한다.
#점3개를 정상적으로 심기 위해선 서로 겹치면 안된다. ->가로 세로로 3이상 거리가 있어야 한다.

for i in range(N):
    for j in range(N):
        #가생이 조건
        if N-1>i>0 and N-1>j>0:
            price = 0
            point = (i,j)
            price+=board[i][j]
            for a,b in direc:
                if N-1>=a+i>=0 and N-1>=b+j>=0:
                    price+=board[a+i][b+j]
                else:
                    break
            else:
                board_price.append((i,j,price))
ans = dfs(0,0,0)
print(ans)

