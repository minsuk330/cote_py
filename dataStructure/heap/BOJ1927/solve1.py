import sys,heapq
def input():
    return sys.stdin.readline().rstrip()

heap = []

N = int(input())

for _ in range(N):
    data = int(input())

    if data==0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap,data)


