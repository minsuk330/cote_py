import sys

def input():
    return sys.stdin.readline().rstrip()

#고이는 빗물의 총량은?
H,W = map(int,input().split())

blocks = list(map(int,input().split()))
left_max = [0]*W
right_max = [0]*W
left_max[0] = blocks[0]
right_max[W-1] = blocks[-1]

for i in range(1,W):
    left_max[i] = max(left_max[i-1],blocks[i])
for i in range(W-2,-1,-1):
    right_max[i] = max(right_max[i+1],blocks[i])
result = 0
for i in range(1,W-1):
    water = min(left_max[i],right_max[i])-blocks[i]
    if water>0:
        result+=water