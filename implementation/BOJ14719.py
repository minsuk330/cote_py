import sys

def input():
    return sys.stdin.readline().rstrip()

#고이는 빗물의 총량은?
H,W = map(int,input().split())

blocks = list(map(int,input().split()))

result  = 0
for i,num in enumerate(blocks):
    #각 인덱스를 기준으로 왼쪽과 오른쪽의 최대 높이를 계산
    if W-1>i>0:
        left = max(blocks[:i+1])
        right = max(blocks[i+1:])
        water = min(left,right)-num
        if water>0:
            result+=water
print(result)