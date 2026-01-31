import sys

def input():
    return sys.stdin.readline().rstrip()

def dfs(left,right,level):
    if left>right:
        return

    mid = (left+right)//2
    
    root = inorders[mid]
    result[level].append(root)
    dfs(left,mid-1,level+1)
    dfs(mid+1,right,level+1)

#루트->왼쪽자식->해당 노드가 왼쪽 자식이 없거나 이미 들어갔다면 종이에 적는다.
#왼->노드>오
#이건 중위순회 성격을 띄고 있다.
K = int(input())
result = [[] for i in range(K)]
inorders = list(map(int,input().split()))
dfs(0,(len(inorders)-1),0)
#총 K개의 줄에 걸쳐서 정답을 출력
#각 노드의 레벨이 I인 빌딩 번호 출력한다. -> 각 트리의 루트를 출력하면 되는 일

for i in range(K):
    print(' '.join(map(str,result[i])))