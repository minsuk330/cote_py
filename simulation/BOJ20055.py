import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

#N벨트 #2N이 이걸 감싸고 돌고있다
#i번의 내구도는 Aj
#각 벨트의 1은 올리는것 N은 내리는 것

#로봇을 올리며 로봇은 스스로 이동이 가능하다.
#로봇을 올리는 위치에 올리거나 로봇이 특정 칸으로 이동하면 내구도 -1
#즉 이동을 당하는 칸은 내구도-1
#벨트가 한칸 회전
#순서: 가장 먼저 올라갓 로봇부터 -> 회전하는 방향으로 이동 가능하면 이동한다.
#이동은 로봇이 없으며 내구도가 1 이상일 경우

#내구도가 0이면 로봇을 올리지 못한다.
#내구도가 0인 칸의 개수가 K개 이상이면 종료한다

N,K = map(int,input().split())
#0~2N까지
dur = deque(map(int,input().split()))
robots = deque([False]*(2*N))
count = 0
level = 0
while count<K:
    level+=1
    #벨트 돌리기
    dur.rotate(1)
    robots.rotate(1)
    #로봇 내리기
    robots[N-1] = False
    #로봇 이동
    #근데 가장 먼저 벨트에 올라간 로봇부터 처리를 해야 함
    #뒤에서부터 처리를 해야하네
    for i in range(N-2,-1,-1):
        if robots[i]==True:
            if robots[i+1]==False and dur[i+1]>0:
                robots[i]=False
                robots[i+1]=True
                dur[i+1]-=1
    robots[N-1] = False

    #로봇 올리기
    if dur[0]>0 and robots[0]==False:
        robots[0]=True
        dur[0]-=1
    
    

    #개수 세기
    count = 0
    for num in dur:
        if num==0:
            count+=1

print(level)