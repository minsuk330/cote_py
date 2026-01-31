import sys

def input():
    return sys.stdin.readline().rstrip()
N = int(input())
calender = [0]*366

for _ in range(N):
    a,b = map(int,input().split())
    for day in range(a,b+1):
        calender[day]+=1

total = 0
width = 0
height = 0

for day in range(1,366):
    if calender[day]>0:
        width+=1
        height = max(height,calender[day])
    else:
        if width>0:
            total += width*height
            width=0
            height=0

if width>0:
    total += width*height
print(total)