import sys

from collections import deque

def input():
    return sys.stdin.readline().rstrip()

#이를 K번 회전시키려 한다. 회전은 시계 Or반시계
#특정 톱니바퀴를 회전시킬 때 옆에 있는 톱니의 극에 따라 다름
#극이 다르다면 반대로 회전, 극이 같으면 회전 X
#rotate+는 시계 -1은 반시계

#입력
#N->0 , S->1
tob = []
check = [0,1,2,3]
rotation = [0,0,0,0]
for _ in range(4):
    line = deque(map(int,input()))
    tob.append(line)

K = int(input())
for _ in range(K):
    #번호,방향
    num,dir = map(int,input().split())
    num_idx = num-1
    rotation = [0,0,0,0]
    rotation[num_idx] = dir

    left_idx = num_idx-1
    while left_idx>=0:
        if tob[left_idx][2]!=tob[left_idx+1][6]:
            rotation[left_idx] = -rotation[left_idx+1]
            left_idx-=1
        else:
            break
    right_idx = num_idx+1
    while right_idx<4:
        if tob[right_idx][6]!=tob[right_idx-1][2]:
            rotation[right_idx] = -rotation[right_idx-1]
            right_idx+=1
        else:
            break
    for i in range(4):
        if rotation[i]!=0:
            tob[i].rotate(rotation[i])

result = 0

if tob[0][0]==1:
    result+=1
if tob[1][0]==1:
    result+=2
if tob[2][0]==1:
    result+=4
if tob[3][0]==1:
    result+=8

print(result)
        



        
