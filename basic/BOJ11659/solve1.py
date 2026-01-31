import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

N,M = map(int,input().split())
numbers = list(map(int,input().split()))

all_sum = [0]*(N+1)
for i in range(1,N+1):
    all_sum[i] = numbers[i-1] + all_sum[i-1]


for _ in range(M):
    a,b = map(int,input().split())
    print(f"{all_sum[b]-all_sum[a-1]}")
        