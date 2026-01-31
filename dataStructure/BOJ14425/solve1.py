import sys

def input():
    return sys.stdin.readline().rstrip()

N,M = map(int,input().split())
input_str = {}
count=0

for i in range(N):
    data = input()
    input_str[data] = i

for _ in range(M):
    test_str = input()
    #input_str을 각 하나씩 도는 for문
    #거기서 또 각 문자씩 돌아야 하는데..ㅇ
    if test_str in input_str:
        count+=1

print(count)

