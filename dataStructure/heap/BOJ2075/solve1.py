import sys,heapq

def input():
    return sys.stdin.readline().rstrip()
heap  = []
N = int(input())


for _ in range(N):
    data = list(map(int,input().split()))

    for num in data:
        heapq.heappush(heap,num)

        if len(heap)>N:
            heapq.heappop(heap)
print(heap[0])

