import sys

#일직선 위 N개의 높이가 서로 다른 탑 설치

N = int(input())

value = list(map(int,input().split()))

result = [0]*N
stack = []

for i in range(N):
    #현재 value보다 낮은 송신탑들은 제거를 해준다.
    while stack and stack[-1][1]<value[i]:
        stack.pop()

    if stack:
        result[i] = stack[-1][0]
    
    # 현재 탑을 스택에 추가한다.
    stack.append((i+1,value[i]))

print(' '.join(map(str,result)))
