import sys

def input():
    return sys.stdin.readline().rstrip()


node_count = int(input())

numbers = list(map(int,input().split()))

node_delete = int(input())

tree = [[] for _ in range(node_count)]
root = -1

for i in range(node_count):
    parent = numbers[i]
    if parent == -1:
        root = i
    else:
        tree[parent].append(i)

#index가 노드
#리스트의 값이 부모
def count_node(node):

    if node == node_delete:
        return 0
    
    if not tree[node]:
        return 1

    count = 0
    for child in tree[node]:
        count += count_node(child)

    return count if count>0 else 1

if root == node_delete:
    print(0)
else:
    print(count_node(root))