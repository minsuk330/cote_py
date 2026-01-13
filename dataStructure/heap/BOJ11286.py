import sys,heapq

def input():
    return sys.stdin.readline().rstrip()

#1.배열에 정수를 넣는다.
#2.배열에서 절대값이 가장 작은 값을 출력하고 제거한다.
#절대값이 가장 작은 값이 여러개일 경우 가장 작은 수를 출력하고
#그 값을 제거한다.
#-힙과 +힙 두개를 운용해야할 것 같은데
N = int(input())
heap_minus = []
heap_plus = []
#-인 경우 -를 붙여서 넣는다. +인 경우 그대로
#최소 값을 출력하는 경우엔?
for _ in range(N):
    num = int(input())

    if num==0:
        if not heap_minus and not heap_plus:
            print(0)
        elif not heap_minus and heap_plus:
            print(heapq.heappop(heap_plus))
        elif not heap_plus and heap_minus:
            print(-heapq.heappop(heap_minus))
        else:
            if heap_minus[0]==heap_plus[0]:
                print(-heapq.heappop(heap_minus))
            elif heap_minus[0]>heap_plus[0]:
                print(heapq.heappop(heap_plus))
            else:
                print(-(heapq.heappop(heap_minus)))
    else:
        if num>0:
            heapq.heappush(heap_plus,num)
        else:
            heapq.heappush(heap_minus,-num)
