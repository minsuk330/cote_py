import sys,heapq

sys.setrecursionlimit(300000)

def input():
    return sys.stdin.readline().rstrip()

N = int(input())

#내가 할 건 루트를 찾기

def inorder(node,level):
    global count
    if node==-1:
        return
    inorder(tree[node][0],level+1)
    xindex[node] = (count,level)
    count+=1
    inorder(tree[node][1],level+1)

tree = {}
#여기에 Level도 같이 부여해야 한다.
xindex = [-1]*(N+1)
parent = [-1]*(N+1)
count = 0

for _ in range(N):
    p,l,r = map(int,input().split())
    tree[p] = (l,r)
    if l != -1: parent[l] = p
    if r != -1: parent[r] = p

root = 0

for i in range(1,N+1):
    if parent[i]==-1:
        root = i
        break

inorder(root,1)

xindex = [x for x in xindex if x != -1]
xindex.sort(key=lambda x: (x[1], x[0]))
result = []
cur_level = xindex[0][1]
lev_min_val = xindex[0][0]
lev_max_val = xindex[0][0]

for x, level in xindex[1:]:
    if level == cur_level:
        lev_max_val = x
    else:
        heapq.heappush(result, (-(lev_max_val - lev_min_val), cur_level))
        cur_level = level
        lev_min_val = x
        lev_max_val = x

heapq.heappush(result, (-(lev_max_val - lev_min_val), cur_level))

# 결과 출력
rest = heapq.heappop(result)
print(rest[1], -rest[0] + 1)