import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())


count = 0

cow = {i:-1 for i in range(1,11)}
for _ in range(N):
    a,b = map(int,input().split())
    if cow[a]==-1:
        cow[a]=b
    else:
        if cow[a]!=b:
            count+=1
            cow[a]=b
print(count)
        
    
