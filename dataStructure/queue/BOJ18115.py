import sys

from collections import deque

def input():
    return sys.stdin.readline().rstrip()

#손에 들린 카드를 내려놓는다.
#1제일 위 1장 바닥에
#2위에서 두번쨰 카드 바닥에 내려놓는다. 2장 이상
#3제일 밑에 있는걸 내려놓는다. 2장 이상\

N = int(input())
data = list(map(int,input().split()))

card = deque()
for i in range(len(data)-1,-1,-1):
    if data[i]==1:
        card.appendleft(N-i)
    elif data[i]==2:
        card.insert(1,N-i)
    else:
        card.append(N-i)

print(' '.join(map(str,card)))


    