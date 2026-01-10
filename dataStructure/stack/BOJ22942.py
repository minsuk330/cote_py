import sys

def input():
    return sys.stdin.readline().rstrip()


N = int(input())
circle = []
edge_point = []
stack = []
circle_check = set()
for i in range(N):
    x,r = map(int,input().split())
    #원 입력 받기
    circle.append((x,r,i))
    #끝점 넣어주기
    edge_point.append((x-r,i))
    edge_point.append((x+r,i))

edge_point.sort()

for i in range(len(edge_point)):
    #새로운 원이다? push
    circle_idx = edge_point[i][1]
    if circle_idx not in circle_check:
        stack.append(edge_point[i])
        circle_check.add(circle_idx)
    else:
        temp = stack.pop()
        if temp[1]!=circle_idx:
            print('NO')
            break
else:
    print('YES')