import sys
def input():
    return sys.stdin.readline().rstrip()
#연산이 열3 행3 대각2
#그리고 H또는 T이고
#이걸 최소 연산횟수를 구하여라
#해당 연산을 구행하거나 수행하지 않거나 둘 중 하나이다.
T = int(input())
def flip_col(board,c):
    for i in range(3):
        board[i][c] ^=1
def flip_row(board,r):
    for i in range(3):
        board[r][i] ^=1
def flip_dia1(board):
    for i in range(3):
        board[i][i]^=1
def flip_dia2(board):
    for i in range(3):
        board[i][2-i]^=1

def is_res(board):
    fir = board[0][0]
    for r in range(3):
        for c in range(3):
            if board[r][c] !=fir:
                return False
    return True

def op(board,k):
    if k < 3:
        flip_row(board, k)
    elif k < 6:
        flip_col(board, k - 3)
    elif k == 6:
        flip_dia1(board)
    else:
        flip_dia2(board)

def dfs(k,count):
    global ans,board
    if count>ans:
        return
    if k==8:
        if is_res(board):
            ans = min(ans,count)
        return

    #연산 수행 x
    dfs(k+1,count)
    #연산 수행
    op(board,k)
    dfs(k+1,count+1)
    op(board,k)
    

for _ in range(T):
    board = []
    ans = float('inf')
    for _ in range(3):
        line = input().split()
        board.append([1 if x=='H' else 0 for x in line])
    dfs(0,0)
    print(-1 if ans==float('inf') else ans)
    