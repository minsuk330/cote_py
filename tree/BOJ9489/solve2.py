import sys

from collections import deque

def input():
    return sys.stdin.readline().rstrip()

while True:
    n,k = map(int,input().split())#n는 노드 개수 k는 타겟
    if n==0 and k==0:
        break
    nodes = list(map(int,input().split()))
    p = 0 #현재 부모 idx -> 이게 포인터 역할을 하는 것이다.
    parent = [-1]*n  #parent의 i즉 nodes의 i번째 부모는 몇번 인덱스인지 저장함
    for i in range(1,n):
        #연속하는 수가 아닐경우
        if nodes[i-1]!=nodes[i]-1:
            p+=1
        parent[i] = p
    idx_target = nodes.index(k)
    idx_parent = parent[idx_target]
    idx_grand = parent[idx_parent]

    if idx_parent==-1:
        print(0)
        continue
    if idx_grand==-1:
        print(0)
        continue
    result = 0
    
    

    #그 다음 grand의 자식들의 개수를 구하면 되는데
    
                
            
                

            
            
    

    

    
    