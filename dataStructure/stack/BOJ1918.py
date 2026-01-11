import sys

from collections import deque

def input():
    return sys.stdin.readline().rstrip()

priority = {'+': 0, '-': 0, '*': 1, '/': 1}

data = input()
stack = []
result = ''

for char in data:
    #피연산자의 경우
    if char.isalpha():
        result+=char
    #괄호의 경우
    elif char == '(':
        stack.append(char)
    #닫는 괄호의 경우
    #여는 괄호 앞까지 출력
    elif char == ')':
        while stack and stack[-1]!='(':
            result+=stack.pop()
        stack.pop()
    #연산자의 경우
    else:
        #현재보다 우선순위가 높거나 같은것 전부 pop
        while stack and stack[-1]!='(' and priority[stack[-1]]>=priority[char]:
            result+=stack.pop()
        stack.append(char)

while stack:
    result+=stack.pop()

print(result)




