import sys

def input():
    return sys.stdin.readline().rstrip()

N,M = map(int,input().split())

bulb = {i:-1 for i in range(1,N+1)}

numbers = list(map(int,input().split()))

for i,num in enumerate(numbers):
    bulb[i+1] = num


for _ in range(M):
    a,b,c = map(int,input().split())
    if a==1:
        bulb[b] = c
    elif a==2:
        for i in range(b,c+1):
            if bulb[i]==0:
                bulb[i]=1
            else:
                bulb[i]=0

    elif a==3:
        for i in range(b,c+1):
            bulb[i] = 0
    else:
        for i in range(b,c+1):
            bulb[i] = 1

print(' '.join(map(str,bulb.values())))
