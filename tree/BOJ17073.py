import sys

def input():
    return sys.stdin.readline().rstrip()

node_count,water = map(int,input().split())
tree = {i:[] for i in range(node_count+1)}

del tree[0]

for _ in range(node_count-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)
leaf_count = 0

for i in range(2,node_count+1):
    if len(tree[i])==1:
        leaf_count+=1

print(water/leaf_count)