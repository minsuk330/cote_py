import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()


N = int(input())
my_stack = deque()
for _ in range(N):
    arr = input().split()
    cmd = arr[0]
    if cmd == 'push':
        my_stack.append(int(arr[1]))
    else:
        if cmd == 'top':
            if len(my_stack)>0:
                print(my_stack[len(my_stack)-1])
            else:
                print('-1')
        elif cmd == 'pop':
            if len(my_stack)>0:
                print(my_stack[len(my_stack)-1])
                my_stack.pop()
            else:
                print('-1')
        elif cmd == 'size':
            print(len(my_stack))
        elif cmd == 'empty':
            if len(my_stack)>0:
                print('0')
            else:
                print('1')
