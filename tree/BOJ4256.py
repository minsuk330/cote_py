import sys

def input():
    return sys.stdin.readline().rstrip()
sys.setrecursionlimit(100000)


T = int(input())
#특정 트리를 전위한것
#중위한 것

def recursion(preleft,preright,inleft,inright,):
    if preleft>preright:
        return
    root = preorder[preleft]
    mid = idx[root]
    leftsize = mid-inleft
    recursion(preleft+1,preleft+leftsize,inleft,mid-1)
    recursion(preleft+1+leftsize,preright,mid+1,inright)
    result.append(root)


#preorder에서 원소를 하나씩 뺀다
#해당 원소를 기준으로 inorder에서 왼,오로 나눈다.
#이걸 반복한다.

for _ in range(T):
    idx = {}
    node_count = int(input())
    preorder = list(map(int,input().split()))
    inorder = list(map(int,input().split()))

    for i,num in enumerate(inorder):
        idx[num] = i

    result = []

    recursion(0,node_count-1,0,node_count-1)

    for i in result:
        print(i,end=' ')
    print()
    

