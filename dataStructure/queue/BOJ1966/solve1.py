import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

N = int(input())

for _ in range(N):
    paper_num,idx = map(int,input().split())
    point = list(map(int,input().split()))
    print_queue = deque((point[i],i) for i in range(paper_num))

    count = 0
    while print_queue:
        current = print_queue.popleft()

        if any(current[0]<num[0] for num in print_queue):
            print_queue.append(current)
        else:
            count+=1
            if current[1]==idx:
                print(count)
                break
