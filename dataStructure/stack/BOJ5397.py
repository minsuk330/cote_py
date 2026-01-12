import sys

def input():
    return sys.stdin.readline().rstrip()


N = int(input())

#내가 처리할껀 백스페이스와 화살표이다.
for _ in range(N):
    data = input()
    left = []
    right = []
    for char in data:
        #중간에 삽입 처리를 어떻게 해야 할지가 고민이지
        if char == '<':
            if left:
                right.append(left.pop())
        elif char == '>':
            if right:
                left.append(right.pop())
        elif char == '-':
            if left:
                left.pop()
        else:
            left.append(char)
            
    print(''.join(map(str,left))+''.join(map(str,reversed(right))))
    

