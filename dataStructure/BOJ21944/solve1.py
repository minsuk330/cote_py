import sys,heapq

def input():
    return sys.stdin.readline().rstrip()

#각 그룹별로 구분
#각 그룹별 level을 전체적으로 관리할 수 있어야 한다.
#알고리즘 분류를 어떻게 관리할까?

def input_proc(number,level,group):
    if group not in max_group_heap:
        max_group_heap[group] = []
    heapq.heappush(max_group_heap[group],(-level,-number))
    if group not in min_group_heap:
        min_group_heap[group] = []
    heapq.heappush(min_group_heap[group],(level,number))

    heapq.heappush(min_all_heap,(level,number))
    heapq.heappush(max_all_heap,(-level,-number))
    heapq.heappush(min_by_level[level], number)
    heapq.heappush(max_by_level[level], -number)

    visited[number] = (level,group)

N = int(input())

max_all_heap = []
min_all_heap = []
min_by_level = [[] for _ in range(101)]
max_by_level = [[] for _ in range(101)]
max_group_heap = {}
min_group_heap = {}
visited = {}
for _ in range(N):
    number,level,group = map(int,input().split())
    input_proc(number,level,group)
    

M = int(input())
for _ in range(M):
    cmds = input().split()
    cmd = cmds[0]
    if cmd=='add':
        number = int(cmds[1])
        level = int(cmds[2])
        group = int(cmds[3])
        input_proc(number,level,group)

    elif cmd=='recommend':
        group = int(cmds[1])
        x = int(cmds[2])

        if x==1:
            heap = max_group_heap.get(group,[])
            while heap:
                level,number = -heap[0][0],-heap[0][1] #최대 값
                if number not in visited or visited[number]!=(level,group):
                    heapq.heappop(heap)
                else:
                    print(number)
                    break
        else:
            #groupt에서 가장 작은 값
            heap = min_group_heap.get(group,[])
            while heap:
                level,number = heap[0][0],heap[0][1] #최대 값
                if number not in visited or visited[number]!=(level,group):
                    heapq.heappop(heap)
                else:
                    print(number)
                    break

    elif cmd == 'recommend2':
        x = int(cmds[1])
        if x==1:
            while max_all_heap:
                level,number = -max_all_heap[0][0],-max_all_heap[0][1] #최대 값
                if number not in  visited or visited[number][0]!=level:
                    heapq.heappop(max_all_heap)
                else:
                    print(number)
                    break
        else:
            while min_all_heap:
                level,number = min_all_heap[0][0],min_all_heap[0][1] #최대 값
                if number not in visited or visited[number][0]!=level:
                    heapq.heappop(min_all_heap)
                else:
                    print(number)
                    break        
    elif cmd=='solved':
        number = int(cmds[1])
        del visited[number]
    else:
        x = int(cmds[1])
        L = int(cmds[2])
        found = False

        if x == 1:
            # level >= L 중 (가장 낮은 level, 그 중 가장 작은 번호)
            for lv in range(L, 101):
                heap = min_by_level[lv]
                while heap:
                    num = heap[0]
                    if num not in visited or visited[num][0] != lv:
                        heapq.heappop(heap)
                    else:
                        print(num)
                        found = True
                        break
                if heap:
                    break
        else:
            # level < L 중 (가장 높은 level, 그 중 가장 큰 번호)
            for lv in range(L - 1, 0, -1):
                heap = max_by_level[lv]
                while heap:
                    num = -heap[0]
                    if num not in visited or visited[num][0] != lv:
                        heapq.heappop(heap)
                    else:
                        print(num)
                        found = True
                        break
                if heap:
                    break
        if not found:
             print(-1)
                

                           




        

        
    
    