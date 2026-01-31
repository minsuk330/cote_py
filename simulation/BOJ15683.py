import sys

def input():
    return sys.stdin.readline().rstrip()
def board_check(c,r,temp_board,direction,cctv_num):
    #1번 배열의 배열 1개
    for d in direction:
        dr,dc = dir[d] #한 방향 정의
        next_r,next_c = dr+r,dc+c
        while N>next_r>=0 and M>next_c>=0 and temp_board[next_r][next_c]!=6:
            if temp_board[next_r][next_c]==0:
                temp_board[next_r][next_c]=-1 #감시 체크 표시
            next_r+=dr
            next_c+=dc
    
def count_board(board):
    count = 0
    for i in range(N):
        for j in range(M):
            if board[i][j]==0:
                count+=1
    return count
def dfs(idx,board):
    global result
    if idx==len(cctvs):
        result = min(result, count_board(board))
        return

    c,r,num = cctvs[idx]

    #여기 for 문으로 특정 cctv의 방향을 돌면서 체크한다.
    for direction in cctv_dir[num]:
        #보드에 감시 영역 표시를 해야 한다.
        #임시 보드를 만들고
        temp_board = [ line[:] for line in board]
        #여기서 보드 체크를 해야 한다.
        board_check(c,r,temp_board,direction,num)
        dfs(idx+1,temp_board)

#상하좌우를 0123으로 표시
cctv_dir = {
    1:[[0],[1],[2],[3]],
    2:[[0,1],[2,3]],
    3:[[0,2],[0,3],[1,2],[1,3]],
    4:[[0,1,2],[0,1,3],[1,2,3],[0,2,3]],
    5:[[0,1,2,3]]
}
#상 하 좌 우
dir = [(1,0),(-1,0),(0,-1),(0,1)] 

cctvs = []#행,열,cctv넘버
result = float('inf')
#세로 가로 
N,M = map(int,input().split())
board = []
for i in range(N):
    line = list(map(int,input().split()))
    board.append(line)

for i in range(N):
    for j in range(M):
        if 0<board[i][j]<6:
            cctvs.append((i,j,board[i][j]))

dfs(0,board)
print(result)
