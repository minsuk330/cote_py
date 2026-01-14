import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())

numbers = list(map(int,input().split()))
nge = [-1]*N
stack = []
for i in range(N):    
    while stack and numbers[stack[-1]]<numbers[i]:
        idx = stack.pop()
        nge[idx] = numbers[i]
    stack.append(i)

print(' '.join(map(str,nge)))