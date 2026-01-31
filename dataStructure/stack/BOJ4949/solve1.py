import sys

def input():
    return sys.stdin.readline().rstrip()


while True:
    stack = []
    data = input()
    is_valid = True
    if data=='.':
        break
    for i,char in enumerate(data):
        if char == '(' or char=='[':
            stack.append(char)

        elif char==')':
            if not stack or stack[-1]!='(':
                is_valid = False
                break
            stack.pop()
        
        elif char==']':
            if not stack or stack[-1]!='[':
                is_valid = False
                break
            stack.pop()
    

    if is_valid and not stack:
        print('yes')
    else:
        print('no')



