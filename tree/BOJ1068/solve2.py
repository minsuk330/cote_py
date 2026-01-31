import sys

def input():
    return sys.stdin.readline().rstrip()

def dfs(target):
    if target not in tree.keys():
        return

    childrens = tree[target][:]
    del tree[target]

    for child in childrens:
        dfs(child)


N = int(input())

numbers = list(map(int,input().split()))
#둘째 줄부터 0번에서 N-1노드까지 각 노드의 부모가 주어진다.
target = int(input())
tree = {i:[] for i in range(N)} #노드번호:(자식1,자식2)
for i in range(N):
    if numbers[i]!=-1:
        tree[numbers[i]].append(i)
dfs(target)

count = 0
for key,value in tree.items():

    if target in value:
        value.remove(target)

    if len(value)==0:
        count+=1

print(count)

