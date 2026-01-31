import sys

def input():
    return sys.stdin.readline().rstrip()
#N은 행 M은 열
N,M,R = map(int,input().split())

dir = {'E':(1,0),'W':(-1,0),'S':(0,1),'N':(0,-1)}  #=>열,행
result = [] #넘어진건F 넘어지지 않은건 S
check = {i:['S']*M for i in range(N)}
board = []
for i in range(N):
    board.append(list(map(int,input().split())))
a = []
d = []
for _ in range(R):
    a.append(input().split()) 
    d.append(list(map(int,input().split())))

a_count = 0
for i in range(R):
    # 공격: 도미노 넘어뜨리기
    row = int(a[i][0])-1 #행
    col = int(a[i][1])-1 #열
    D = a[i][2]
##X행 Y열
    if check[row][col] == 'S':  # 이미 서 있는 도미노만 넘어뜨릴 수 있음
        dc,dr = dir[D] #열,행
        height = board[row][col]
        check[row][col] = 'F'
        a_count += 1

        nr,nc = row+dr,col+dc
        remaning = height-1

        while remaning>0 and N>nr>=0 and M>nc>=0:
            if check[nr][nc]=='S':
                check[nr][nc] = 'F'
                a_count+=1
                remaning = max(remaning-1,board[nr][nc]-1)
            else:
                remaning-=1
            
            nr += dr
            nc += dc
    
    row = int(d[i][0])-1
    col = int(d[i][1])-1
    check[row][col] = 'S'


print(a_count)
for i in range(N):
    print(' '.join(check[i]))