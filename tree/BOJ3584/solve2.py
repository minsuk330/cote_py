import sys

def input():
    return sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    N = int(input())
    tree = [0]*(N+1)
    visited = [False]*(N+1)
    for _ in range(N-1):
        parent,child = map(int,input().split())
        tree[child] = parent

    node1,node2 = map(int,input().split())
    current = node1
    while current!=0:
        visited[current]=True
        current = tree[current]

    current = node2

    while not visited[current]:
        current = tree[current]

    print(current)


    
