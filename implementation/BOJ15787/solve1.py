import sys

def input():
    return sys.stdin.readline().rstrip()

N,M = map(int,input().split())
#N개의 기차를 만들어야 한다.
trains = {i:[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] for i in range(1,N+1)}



for _ in range(M):
    cmds = list(map(int,input().split()))
    cmd = cmds[0]
    
    if cmd==1:
        i = cmds[1]
        x = cmds[2]
        trains[i][x-1] = 1
    elif cmd==2:
        i = cmds[1]
        x = cmds[2]
        trains[i][x-1] = 0
    elif cmd==3:
        i = cmds[1]
        #전부 뒤로 이동시키기
        new_train = [0]*20
        for j in range(19):
            new_train[j+1] = trains[i][j]
        trains[i] = new_train
    else:
        i = cmds[1]
        #전부 앞으로 이동시키기
        new_train = [0]*20
        for j in range(1,20):
            new_train[j-1] = trains[i][j]
        trains[i] = new_train
unique_train = []

for train in trains.values():
    if train not in unique_train:
        unique_train.append(train)
print(len(unique_train))