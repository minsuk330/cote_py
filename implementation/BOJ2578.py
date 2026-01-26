import sys

def input():
    return sys.stdin.readline().rstrip()

board = {}
check_num = {}
check = {i:[-1,-1,-1,-1,-1,-1] for i in range(1,6)}
dr = [(1,1),(2,2),(3,3),(4,4),(5,5)]
dl = [(1,5),(2,4),(3,3),(4,2),(5,1)]
def bingo():
    bingo_count = 0
    #가로 체크
    for i in range(1,6):
        line = check[i]
        line_count = 0
        for num in line:
            if num == 1:
                line_count+=1
        if line_count==5:
            bingo_count+=1

    #세로 체크
    for i in range(1,6):
        row_count=0
        for j in range(1,6):
            if check[j][i]==1:
                row_count+=1
        if row_count==5:
            bingo_count+=1
            row_count=0
    #대각선 체크
    dr_count = 0
    for a,b in dr:
        if check[a][b]==1:
            dr_count+=1
    if dr_count==5:
        bingo_count+=1
    dl_count = 0
    for a,b in dl:
        if check[a][b]==1:
            dl_count+=1
    if dl_count==5:
        bingo_count+=1
    return bingo_count
        

for i in range(1,6):
    line = list(map(int,input().split()))
    for j,num in enumerate(line):
        board[num] = (i,j+1)

for i in range(1,6):
    line = list(map(int,input().split()))
    check_num[i] = line
found = False
result = 0
for i in range(1,6):
    line = check_num[i]
    for j,num in enumerate(line):
        result+=1
        a,b = board[num]
        check[a][b] = 1
        count = bingo()
        if count>=3:
            print(result)
            found=True   
            break
    if found:
        break

