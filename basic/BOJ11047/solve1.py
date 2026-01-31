import sys

def input():
    return sys.stdin.readline().rstrip()


N,K = map(int,input().split())
numbers = []
for _ in range(N):
   num = int(input())
   numbers.append(num)


count = 0

for i in range(N-1, -1, -1):
    if K >= numbers[i]:
        count +=K//numbers[i]
        K %= numbers[i]
    
    if K == 0:
        break

print(count)
