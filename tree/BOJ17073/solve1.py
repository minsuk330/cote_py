import sys

from collections import deque

def input():
    return sys.stdin.readline().rstrip()


def dfs(node,parent):
    children = []

    for child in tree[node]:
        if child!=parent:
            children.append(child)

    if not children:
        return 1

    count = 0

    for child in children:
        count+=dfs(child,node)
    return count


def bfs():
    while queue:
        node = queue.popleft()
        childs = []

        if not childs and node!=1:
            leaf_count+=1

        for child in tree[node]:
            visited[child] = True
            queue.append(child)
          
node_count,water = map(int,input().split())
tree = {i:[] for i in range(node_count+1)}

visited = [False]*(node_count+1)
queue = deque()
queue.append(1)

visited[1] = True

leaf_count = 0
del tree[0]







for _ in range(node_count-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)
leaf_count = 0

for i in range(2,node_count+1):
    if len(tree[i])==1:
        leaf_count+=1

print(water/dfs(1,-1))


##dfs





##bfs