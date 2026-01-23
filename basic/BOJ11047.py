import sys

def input():
    return sys.stdin.readline().rstrip()


N,K = map(int,input().split())
numbers = []
for _ in range(N):
   num = int(input())
   numbers.append(num)


count = 0

while True:
    num = numbers.pop()
    if K<num:
        continue
    elif K>=num:
        count+=1
        K-=num
        numbers.append(num)
    if K==0:
        break
print(count)