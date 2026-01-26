import sys

from collections import deque

def input():
    return sys.stdin.readline().rstrip()

arr = input()

stack = deque()
flag = False
result = []
#각 문자열의 단위를 나눠서 각 단위마다 거꾸로 출력한다.
#이때 나누는 단위는 띄어쓰기가 기본
#<>로 감싸져 있는건 무시, 
#<>로 구분된 단어는 하나의 문자열의 단위가 된다.
        
temp = []
for char in arr:
    if char=='<':
        while stack:
            print(stack.pop(), end='')
        flag=True
        temp.append(char)
        continue
    elif char=='>':
        temp.append(char)
        print(''.join(temp), end='')
        temp=[]
        flag=False
        continue
    elif flag==True:
        temp.append(char)
        continue
    elif flag==False:
        if char!=' ':
            stack.append(char)
        else:
            while stack:
                print(stack.pop(),end='')
            print(' ',end='')

while stack:
    print(stack.pop(),end='')
print()