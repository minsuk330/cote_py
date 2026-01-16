import sys

def input():
    return sys.stdin.readline().rstrip()

#루트
#왼쪽 x->왼쪽
#오른쪽 자식->부모

def recur(arr,level):
    if not arr:
        return
    mid = len(arr)//2

    result[level].append(arr[mid])

    recur(arr[:mid],level+1)
    recur(arr[mid+1:],level+1)
    
N = int(input())

tree = []
numbers = list(map(int,input().split()))
result = [[] for _ in range(N)]

recur(numbers,0)

for i in range(N):
    res = result[i]
    print(' '.join(map(str,res)))
