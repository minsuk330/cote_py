import sys

def input():
    return sys.stdin.readline().rstrip()

stack = input()
count = 0
temp_stack = []

for i in range(len(stack)):
    if stack[i]=='(':
        temp_stack.append('(')
    else:
        temp_stack.pop()
        #레이저인가?
        if stack[i-1]=='(':
            count+=len(temp_stack)
        else:
            count+=1

print(count)