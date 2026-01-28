import sys
sys.setrecursionlimit(100000)
def input():
    return sys.stdin.readline().rstrip()


nodes = []


def find_last_node(node):
    if node==-1:
        return
    find_last_node(tree[node][0])
    nodes.append(node)
    find_last_node(tree[node][1])

N = int(input())
check = {i:False for i in range(1,N+1)}
tree = {i:(0,0) for i in range(1,N+1)}
parent = {}

for _ in range(N):
    p,l,r = map(int,input().split())
    tree[p] = (l,r)
    if l!=-1:
        parent[l] = p
    if r!=-1:
        parent[r] = p
find_last_node(1)
last_node = nodes[-1]

cur = 1
count = 0

while True:
    l, r = tree[cur]
    # 왼쪽 자식이 있고 아직 방문 안했으면
    if l != -1 and not check[l]:
        check[cur] = True
        cur = l
        count += 1
    # 오른쪽 자식이 있고 아직 방문 안했으면
    elif r != -1 and not check[r]:
        check[cur] = True
        cur = r
        count += 1
    # 마지막 노드면 종료
    elif cur == last_node:
        break
    else:
        count+=1
        check[cur]=True
        cur=parent[cur]

print(count)
        