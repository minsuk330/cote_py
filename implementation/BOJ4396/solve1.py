import sys

def input():
    return sys.stdin.readline().rstrip()

#지뢰가 없는 지점을 건드리면 상하좌우,대각선에 지뢰가 몇개인지 알려준다.

#
n = int(input())

#x는 이미 열린 칸
#열리지않은 칸은 .이다
result ={i:[]for i in range(1,n+1)} 
board = {i:[]for i in range(1,n+1)}
mine_click = {i:[]for i in range(1,n+1)}
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

#실제 지뢰
for i in range(1,n+1):
    line = input()
    for char in line:
        board[i].append(char)

for i in range(1,n+1):
    line = input()
    for char in line:
        mine_click[i].append(char)
mine_hit = False
for i in range(1,n+1):
    line = mine_click[i]
    for j,char in enumerate(line):
        ##사용자 클릭
        if char=='x':
            #클릭이 지뢰인 경우
            if board[i][j]=='*':
                mine_hit = True
                result[i].append('*')

            #클릭이 지뢰가 아닌 경우 주변 지뢰 갯수를 세야 한다.
            else:
                #i는 열 j는 행
                count=0
                for a,b in directions:
                    ta,tb = i+a,j+b
                    if n>=ta>=1 and n>tb>=0:
                        if board[ta][tb]=='*':
                            count+=1
                result[i].append(count)
                    
        #클릭 안함
        else:
            result[i].append('.')
if mine_hit:
    for i in range(1,n+1):
        line = board[i]
        for j,num in enumerate(line):
            if num=='*' and mine_click[i][j] != 'x':
                result[i][j] = '*'
        
for i in range(1,n+1):
    line = result[i]
    print(''.join(map(str,line)))
