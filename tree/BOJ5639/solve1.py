import sys

def input():
    return sys.stdin.readline().rstrip()

sys.setrecursionlimit(200000)

#왼쪽 서브트리의 있는 모든 노드의 키는 노드의 키보다 작음
#오른쪽은 더 크다
#왼쪽 오른쪽 서브 트리도 이진 검색 트리이다.

def recursion(left,right):
    if left>=right:
        return
    
    mid = left+1

    while mid<right and preorder[mid]<preorder[left]:
        mid+=1

    recursion(left+1,mid)
    recursion(mid,right)
    print(preorder[left])
     
preorder = []

while True:
    line = input()
    if not line:
        break
    preorder.append(int(line))
right = len(preorder)
recursion(0,right)

