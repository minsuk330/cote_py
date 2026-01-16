import sys

def input():
    return sys.stdin.readline().rstrip()

node_count = int(input())

def delete(node):
    if node is None or node not in tree:
        return
    if tree[node]==[]:
        del tree[node]
        return
    if len(tree[node]) == 2:
        left, right = tree[node]
    elif len(tree[node]) == 1:
        left = tree[node][0]
        right = None
    else:
        left = right = None
    delete(left)
    delete(right)
    
numbers = list(map(int,input().split()))
tree = {i:[] for i in range(node_count)}
for i in range(len(numbers)):
    #루트 노드 처리
    parent = numbers[i]
    if parent!=-1:
        tree[parent].append(i)

node_delete = int(input())
delete(node_delete)

if node_delete == -1:
    print(0)
else:
    delete(node_delete)
    if numbers[node_delete] != -1:
        parent = numbers[node_delete]
        if parent in tree and node_delete in tree[parent]:
            tree[parent].remove(node_delete)

    count = 0
    for key, value in tree.items():
        if value == []:
            count += 1
    print(count)
