import sys

def input():
    return sys.stdin.readline().rstrip()
sys.setrecursionlimit(200000)

##인오더와 포스트오더가 주어지면 프리오더를 구하여라

def recursion(in_l,in_r,po_l,po_r):
    #각 나눈 구간의 가장 마지막 값을 넣어야 한다.
    if in_l>in_r:
        return
    

    root = postorder[po_r]

    mid_idx = in_idx[root]

    left_size = mid_idx-in_l #왼쪽 원소의 갯수야
    result.append(root)
    recursion(in_l,mid_idx-1,po_l,left_size-1+po_l)
    recursion(mid_idx+1,in_r,left_size+po_l,po_r-1)


N = int(input())

in_idx = {}


inorder = list(map(int,input().split()))
postorder = list(map(int,input().split()))
for i,num in enumerate(inorder):
    in_idx[num] = i


result = []

recursion(0,N-1,0,N-1)

print(*result)