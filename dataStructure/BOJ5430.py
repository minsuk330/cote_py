import sys

from collections import deque

def input():
    return sys.stdin.readline().rstrip()

N = int(input())

for _ in range(N):
    func = input()
    arr_size = int(input())
    data = input()
    #1이면 순 -1이면 역방향
    direction_flag = 1

    # 배열 파싱
    if arr_size > 0:
        arr = deque(map(int, data[1:-1].split(',')))
    else:
        arr = deque()

    for char in func:
        if char == 'R':
            direction_flag *=-1
        else:
            if arr:
                if direction_flag>0:
                    arr.popleft()
                else:
                    arr.pop()
            else:
                print('error')
                break

    else:
        if direction_flag>0:
            print('['+','.join(map(str,arr))+']')
        else:
            print('['+','.join(map(str,reversed(arr)))+']')
        