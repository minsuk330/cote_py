import sys

def input():
    return sys.stdin.readline().rstrip()

sys.setrecursionlimit(200000)

#트리의 존재하는 길이중 가장 긴 것
#각 노드와 노드 사이의 간선의 크기를 구해서 가장 큰 값을 구해야 한다.
#각 리프노드의 거리의 최대 값을 구하면 될듯한대..
#부모로부터 가장 긴 간선을 가진 노드를 구한다.
#해당 노드로부터 가장 멀리 떨어진 노드를 구한다.

def dfs(root,parent,value):
    max_node,max_value = root,value
    
    for node,dist in tree[root]:
        if parent==node:
            continue
        n,d = dfs(node,root,dist+value)

        if d>max_value:
            max_node = n
            max_value = d
    return max_node,max_value
    
    

N = int(input())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    parent,child,value = map(int,input().split())
    tree[parent].append((child,value))
    tree[child].append((parent,value))

first_node,value = dfs(1,0,0)

second_node,result = dfs(first_node,0,0)

print(result)

