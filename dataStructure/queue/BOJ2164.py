import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()


N = int(input())

#위에꺼 버리고 그 다음꺼 넣고 -> 카드가 한 장 남을때 까지

arr = deque(range(1,N+1))

while len(arr)>1:
    arr.popleft()
    arr.append(arr.popleft())
print(arr[0])