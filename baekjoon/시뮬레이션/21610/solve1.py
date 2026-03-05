import sys
def input():
  return sys.stdin.readline().rstrip()
#i번째 이동 명령은 방향 d와 거리 s로 이뤄져 있으며 방향은 8방향
direc = [(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]

N,M = map(int,input().split())

board = []
groom = [[False]*N for _ in range(N)]

for _ in range(N):
  line = list(map(int,input().split()))
  board.append(line)

#비바라기 시전
groom[N-1][0] = True
groom[N-1][1] = True
groom[N-2][0] = True
groom[N-2][1] = True

def calculate_rc(dr,dc,i,j):
  row = (i+dr)%N
  col = (j+dc)%N
  return (row,col)
  
for _ in range(M):
  d,s = map(int,input().split())

  # 현재 구름 위치를 먼저 수집
  current_grooms = []
  for i in range(N):
    for j in range(N):
      if groom[i][j]:
        current_grooms.append((i,j))

  # 구름 초기화
  groom = [[False]*N for _ in range(N)]

  # 수집된 구름들을 이동
  new_grooms = set()
  for i, j in current_grooms:
    dr, dc = (direc[d-1][0]*s, direc[d-1][1]*s)
    row, col = calculate_rc(dr, dc, i, j)
    groom[row][col] = True
    new_grooms.add((row, col))
    board[row][col] += 1

  # 구름 모두 사라져야 함
  groom = [[False]*N for _ in range(N)]

  #이제 여기서 조건4 달아주기
  for r,c in new_grooms:
    water = 0
    #대각선 방향 4방향
    for i in range(1,8,2):
      dr,dc = direc[i]
      if 0<=r+dr<N and 0<=c+dc<N:
        if board[r+dr][c+dc]>0:
          water+=1
    board[r][c]+=water

  for i in range(N):
    for j in range(N):
      if board[i][j]>=2 and (i,j)not in new_grooms: #이게 이전에 사라진 구름인지 체크해야 함
        groom[i][j] = True
        board[i][j]-=2


result = 0
for line in board:
  result+=sum(line)

print(result)
  
        
        
        
        
        
        

      

      
        

  