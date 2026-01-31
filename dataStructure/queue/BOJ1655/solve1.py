import sys,heapq

def input():
    return sys.stdin.readline().rstrip()


N = int(input())

#각 정수가 들어오면 중간 값을 출력
#만약 짝수번째 수라면 중간의 두 수중 작은 수

right_heap = []#중앙값 이후 값들
left_heap = []#1~중앙값

for _ in range(N):
    #입력이 들어와
    #left삽입
    #그 다음 값이 이전 값 보다 작거나 같다 left 삽입
    num = int(input())
    if not left_heap or -left_heap[0]>=num:
        heapq.heappush(left_heap,-num)
    else:
        heapq.heappush(right_heap,num)

    #균형 맞추기
    if len(left_heap)<len(right_heap):
        heapq.heappush(left_heap,-heapq.heappop(right_heap))
    elif len(left_heap)>len(right_heap)+1:
        heapq.heappush(right_heap,-heapq.heappop(left_heap))

    print(-left_heap[0])
        
        
        
