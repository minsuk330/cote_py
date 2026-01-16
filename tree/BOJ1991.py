import sys

def input():
    return sys.stdin.readline().rstrip()

#전위중위후위 결과 출력

def perorder_traversal(node):
    if node=='.':
        return
    print(node,end='')
    perorder_traversal(tree[node][0])
    perorder_traversal(tree[node][1])

def inorder_traversal(node):
    if node=='.':
        return
    inorder_traversal(tree[node][0])
    print(node,end='')
    inorder_traversal(tree[node][1])
    

def postorder_traversal(node):
    if node=='.':
        return
    postorder_traversal(tree[node][0])
    postorder_traversal(tree[node][1])
    print(node,end='')

N = int(input())

tree = {}
for _ in range(N):
    parent,child1,child2 = input().split()
    tree[parent] = (child1,child2)
    
perorder_traversal('A')
print()
inorder_traversal('A')
print()
postorder_traversal('A')
print()