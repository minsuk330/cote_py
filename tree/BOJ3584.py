import sys

def input():
    return sys.stdin.readline().rstrip()
sys.setrecursionlimit(200000)
#두 노드의 공통조상을 구하여라
#이 중 깊이가 가장 깊은 것을 찾아야 한다.
#각 노드의 부모들을 넣는다.
#가장 처음 들어간 값이 깊이가 ㅅ깊음
T = int(input())

def dfs(child,parents):
    parents.append(child)
    ##부모가 있다면
    if tree[child]!=[]:
        return dfs(tree[child][0],parents)
    else:
        return



for _ in range(T):
    N = int(input())
    tree = [[] for _ in range(N+1)]
    parent1 = []
    parent2 = []
    for _ in range(N-1):
        parent,child = map(int,input().split())
        tree[child].append(parent)

    node1,node2 = map(int,input().split())
    dfs(node1,parent1)
    dfs(node2,parent2)
    for num in parent1:
        if num in parent2:
            print(f"{num}")
            break

    
