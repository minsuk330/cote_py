import sys

def input():
    return sys.stdin.readline().rstrip()
sys.setrecursionlimit(200000)

N = int(input())

count = 0

numbers = []

def insert(x,root,cnt):
    global count
    count+=cnt
    
    if x<root:
        left,right = tree[root]
        if left==-1:
            tree[root] = (x,right)
            return count
        else:
            return insert(x,left,1)
    else:
        left,right = tree[root]
        if right==-1:
            tree[root] = (left,x)
            return count
        else:
            return insert(x,right,1)

for _ in range(N):
    numbers.append(int(input()))
tree = {i:(-1,-1) for i in numbers}
root = 0
for i,num in enumerate(numbers):
    if i==0:
        root = num
        print(0)
    else:
        print(insert(num,root,1))