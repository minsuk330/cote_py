import sys

from collections import deque

def input():
    return sys.stdin.readline().rstrip()

N,M = map(int,input().split())

arr = deque(range(1,N+1))
result = []

for _ in range(N):
    arr.rotate(-(M-1))
    result.append(arr.popleft())

print('<'+', '.join(map(str,result))+'>')
 