import sys

from collections import deque

def input():
    return sys.stdin.readline().rstrip()

N = int(input())

tree = [[] for _ in range(N+1)]
parent = [0]*(N+1)

for _ in range(N-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

queue = deque([1])

parent[1] = 1

##이제 탐색을 시작 해야 함

while queue:
    node = queue.popleft()

    for child in tree[node]:
        if parent[child]==0:
            parent[child] = node
            queue.append(child)

for i in range(2,N+1):
    print(parent[i])