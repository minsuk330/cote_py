import sys,heapq

def input():
    return sys.stdin.readline().rstrip()

max_rec_prob = []
min_rec_prob = []

N = int(input())
visited = {}
for _ in range(N):
    number,level = map(int,input().split())
    #이걸로level정렬과 number정렬 같이 진행한다.
    heapq.heappush(max_rec_prob,(-level,-number))
    heapq.heappush(min_rec_prob,(level,number))
    visited[number] = level

M = int(input())

for _ in range(M):
    cmds = input().split()
    cmd = cmds[0]
    #추가
    if cmd=='add':
        number = int(cmds[1])
        level = int(cmds[2])
        heapq.heappush(max_rec_prob,(-level,-number))
        heapq.heappush(min_rec_prob,(level,number))
        visited[number] = level
        
    #삭제 O(N)보다 작아야 한다.
    elif cmd=='solved':
        number = int(cmds[1])
        del visited[number]
    #최대 최소 값 추출
    else:
        cmd1=int(cmds[1])
        # 최대 값 추출
        if cmd1==1:
            while max_rec_prob:
                level = -max_rec_prob[0][0]
                number = -max_rec_prob[0][1]
                if number not in visited or visited[number]!=level:
                    heapq.heappop(max_rec_prob)
                else:
                    print(number)
                    break
                    
        else:
            while min_rec_prob:
                level = min_rec_prob[0][0]
                number = min_rec_prob[0][1]
                if number not in visited or visited[number]!=level:
                    heapq.heappop(min_rec_prob)
                else:
                    print(number)
                    break


