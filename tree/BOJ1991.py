import sys

def input():
    return sys.stdin.readline().rstrip()

def preorder(node):
    if node=='.':
        return
    print(node, end='')
    preorder(tree[node][0])
    preorder(tree[node][1])

def inorder(node):
    if node=='.':
        return
    inorder(tree[node][0])
    print(node, end='')
    inorder(tree[node][1])

def postorder(node):
    if node=='.':
        return
    postorder(tree[node][0])
    postorder(tree[node][1])
    print(node,end='')
    

tree = {}

N = int(input())

for _ in range(N):
    parent,c1,c2 = map(str,input().split())

    tree[parent] = (c1,c2)

preorder('A')
print()
inorder('A')
print()
postorder('A')
print()