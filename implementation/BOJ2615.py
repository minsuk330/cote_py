import sys

def input():
    return sys.stdin.readline().rstrip()
board = {}
directions = [(0,1), (1,0), (1,1), (-1,1)]
def is_five(dy,dx,sy,sx,num):
    global o_count
    next_y =sy+dy
    next_x = sx+dx
    if 19>next_y>=0 and 19>next_x>=0:
        if board[next_y][next_x]==num:
            o_count+=1
            is_five(dy,dx,next_y,next_x,num)
        else:
            return


for i in range(19):
    numbers = list(map(int,input().split()))
    board[i] = numbers

for k,v in board.items():
    for i,num in enumerate(v):
        if num==1 or num==2:
            start = (k,i)
            for a,b in directions:
                if 19>k-a>=0 and 19>i-b>=0:
                    if board[k-a][i-b]==num:
                      continue  # 이 방향은 중간이므로 체크 안 함
                o_count = 1
                if 19>a+k>=0 and 19>b+i>=0:
                    if board[a+k][b+i]==num:
                        o_count+=1
                        is_five(a,b,a+k,b+i,num)
                if o_count==5:
                    print(num)
                    print(k+1,i+1)
                    exit()
                    break
print(0)

