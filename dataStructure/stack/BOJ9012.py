import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())

for _ in range(N):
    arr = input()
    stack = []

    for temp in arr:
        if temp == '(':
            stack.append(temp)
        elif temp == ')':
            if len(stack) == 0:
                print('NO')
                break
            stack.pop()
    else:
        if len(stack) == 0:
            print('YES')
        else:
            print('NO')


