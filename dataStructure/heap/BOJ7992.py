import sys,heapq
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

#이중 우선순위 큐
#데이터 삭제 시 우선순위가 가장 높거나 낮은 데이터중 하나 선택
#
T = int(input())

for _ in range(T):
    ope_count = int(input())
    max_heap = []
    min_heap = []
    visited = {}
    for _ in range(ope_count):
        cmd,num = input().split()
        num = int(num)
        if cmd == 'I':
            heapq.heappush(max_heap,-num)
            heapq.heappush(min_heap,num)
            visited[num] = visited.get(num,0)+1
        else:
            #최대값 삭제
            if num == 1:
                
                while max_heap and visited[-max_heap[0]]==0:
                    heapq.heappop(max_heap)
                #최대 힙에서 삭제한건 최소 힙에서도 반영을 해줘야 한다.
                if max_heap:
                    value = -heapq.heappop(max_heap)
                    visited[value]-=1
            else:
                while min_heap and visited[min_heap[0]]==0:
                    heapq.heappop(min_heap)
                if min_heap:
                    value = heapq.heappop(min_heap)
                    visited[value]-=1

    while min_heap and visited[min_heap[0]]==0:
        heapq.heappop(min_heap)

    while max_heap and visited[-max_heap[0]]==0:
        heapq.heappop(max_heap)


    
    if min_heap and max_heap:
        print(f"{-max_heap[0]} {min_heap[0]}")
        
    else:
        print("EMPTY")