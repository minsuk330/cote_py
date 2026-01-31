import sys

def input():
    return sys.stdin.readline().rstrip()

input_stack = input()
stack = []
for i in range(len(input_stack)):
    current = input_stack[i]
    #여는 괄호
    if current=='(' or current=='[':
        stack.append(current)
    #닫는 괄호 일 때 숫자와 올바른 괄호 아닌 괄호에 대해 각각 검사
    #닫는 괄호일 경우 2 push 
    #숫자일 경우 temp에 값 추가
    #만약 temp가 이미 계산된 경우라면 *수행

    #닫는 괄호 1
    elif current == ')':
        temp = 0
        while stack:
            top = stack.pop()
            if top=='(':
                if temp==0:
                    stack.append(2)
                else:
                    stack.append(temp*2)
                break
            elif top=='[':
                print(0)
                exit()
            else:
                temp+=top
        else:
            print(0)
            exit()
    elif current == ']':
        temp = 0
        while stack:
            top = stack.pop()
            if top=='[':
                if temp==0:
                    stack.append(3)
                else:
                    stack.append(temp*3)
                break
            elif top=='(':
                print(0)
                exit()
            else:
                temp+=top
        else:
            print(0)
            exit()
if any(x in stack for x in ['(', '[', ')', ']']):
    print(0)
else:
    print(sum(stack))