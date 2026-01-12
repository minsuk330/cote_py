import sys

from collections import deque

def input():
    return sys.stdin.readline().rstrip()


#원소를 뽑아내는건 첫번재 원소만 가능하다
#1번째 원소 뽑아내기 -> 기존 큐 원소 값 1씩 증가
#왼쪽으로 회전 맨 앞 원소 맨 뒤로- rotate(-)
#오른쪽으로 회전 rotate(+)
#N큐의 크기, M뽑아내는 수의 갯수
#둘째줄은 수의 위치 num
N,M = map(int,input().split())

data = list(map(int,input().split()))
#오른쪽 왼쪽 회전 또는 원소 추출을 통해서 원하는 값을 뽑아야 한다.

queue = deque(i+1 for i in range(N))

count = 0
for num in data:
    idx = queue.index(num)
    
    if idx <= len(queue) - idx:
        queue.rotate(-idx)
        count += idx
    else:
        queue.rotate(len(queue) - idx)
        count += len(queue) - idx
    
    queue.popleft()  # 회전 후 항상 제거


print(count)