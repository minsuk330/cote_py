import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
my_queue = deque()
for _ in range(N):
    arr = input().split()
    cmd = arr[0]
    if cmd == 'push':
        my_queue.append(int(arr[1]))
    else:
        if cmd == 'front':
            if len(my_queue)>0:
                print(my_queue[0])
            else:
                print('-1')
        elif cmd == 'pop':
            if len(my_queue)>0:
                print(my_queue[0])
                my_queue.popleft()
            else:
                print('-1')
        elif cmd == 'size':
            print(len(my_queue))
        elif cmd == 'empty':
            if len(my_queue)>0:
                print('0')
            else:
                print('1')
        else:
            if len(my_queue)>0:
                print(my_queue[len(my_queue)-1])
            else:
                print('-1')

