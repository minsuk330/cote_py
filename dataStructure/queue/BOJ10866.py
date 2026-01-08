import sys


def input():
    return sys.stdin.readline().rstrip()

my_deque = []

N = int(input())

for _ in range(N):
    cmd = input().split()

    if len(cmd)==2:
        fir = cmd[0]
        if fir=='push_back':
            my_deque.append(cmd[1])
        else:
            my_deque.insert(0,cmd[1])

    else:
        fir = cmd[0]
        if fir=='front':
            print(my_deque[0]) if my_deque else print(-1)
        elif fir=='back':
            if len(my_deque)>=1:
                print(my_deque[-1])
            else:
                print('-1')
        elif fir=='empty':
            if len(my_deque)>=1:
                print('0')
            else:
                print('1')
        elif fir=='size':
            print(len(my_deque))
        elif fir =='pop_back':
            if len(my_deque)>=1:
                print(my_deque.pop())
            else:
                print('-1')
        else:
            if len(my_deque)>=1:
                print(my_deque.pop(0))
            else:
                print('-1')

        




