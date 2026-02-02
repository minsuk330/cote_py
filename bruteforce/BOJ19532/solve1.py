import sys

def input():
    return sys.stdin.readline().rstrip()


a,b,c,d,e,f = map(int,input().split())

#x와 y를 출력하라

rx,ry=0,0

for x in range(-999,1000):
    for y in range(-999,1000):
        if (a*x+b*y)==c and d*x+e*y==f:
            rx=x
            ry=y
print(rx,ry)
            