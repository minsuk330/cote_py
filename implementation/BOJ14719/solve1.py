import sys

def input():
    return sys.stdin.readline().rstrip()

#고이는 빗물의 총량은?
H,W = map(int,input().split())

blocks = list(map(int,input().split()))

l,r = 0,W-1

lmax,rmax = blocks[l],blocks[r]

result = 0

while l<r:
    if lmax<=rmax:
        l+=1
        lmax = max(lmax,blocks[l])
        result+=max(0,lmax-blocks[l])
    else:
        r-=1
        rmax = max(rmax,blocks[r])
        result+=max(0,rmax-blocks[r])
