import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
data = list(map(int,input().split()))

balloon = deque((i+1,data[i]) for i in range(N))

result = []
for i in range(N):
        num,paper = balloon.popleft()
        result.append(num)
        
        if paper >0:
            balloon.rotate(-(paper-1))
        else:
            balloon.rotate(-(paper))
        

print(' '.join(map(str,result)))
