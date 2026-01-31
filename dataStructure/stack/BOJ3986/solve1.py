import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())

count = 0
for _ in range(N):
    stack = []
    data = input()

    for char in data:
        #pop을 하는 경우
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    if not stack:
        count+=1
            
print(count)

    