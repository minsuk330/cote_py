import sys

def input():
    return sys.stdin.readline().rstrip()


#하루 한 시간 단위로 일을 함
#한 시간 일->피로도A만큼 B만큼 처리
#한시간 쉼 ->C만큼 줄어듬
#피로도가 - 이면 0

#피로도를 M이상 넘지 않게 일을 시키려 한다.
#하루 24시간 안에 피로도 M을 넘지 않고 최대 일 수 
#그러면 총 시간*A가 M을 넘지 않도록 하는게 중요하다

A,B,C,M = map(int,input().split())
#10 5 1 10
tired = 0
result = 0
for i in range(24):
    #일을 수행
    if A+tired<=M:
        result+=B
        tired+=A
    #휴식 수행
    else:
        tired-=C
        if tired<0:
            tired=0

print(result)