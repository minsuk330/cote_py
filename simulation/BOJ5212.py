import sys

def input():
    return sys.stdin.readline().rstrip()

#다도해의 지도 R*C
#X는 땅 .  은 바다
#50년 후엔 인접한 3칸또는 4칸에 바다가 있는 땅은 모두 잠긴다.
#50년후 지도를 그려보자
#지도의 범위를 벗어나는 곳은 모두 바다이다.

R,C = map(int,input().split())

dir = [(-1,0),(1,0),(0,1),(0,-1)]
jido = []
for _ in range(R):
    m = input()
    jido.append(m)
result = [['.' for _ in range(C)]for _ in range(R)]
for i in range(R):
    for j in range(C):
        char = jido[i][j]
        if char=='X':
            sea_count = 0
            for a,b in dir:
                nx = b+j
                ny = a+i
                if 0<=nx<C and 0<=ny<R:
                    if jido[ny][nx]=='.':
                        sea_count+=1
                else:
                    sea_count+=1

            if sea_count<3:
                result[i][j]='X'
#이제 최소 직사각형 찾기
rows = [i for i in range(R) if 'X' in result[i]]

top, bottom = rows[0], rows[-1]
left = C
right = -1

for arr in result:
    for i,char in enumerate(arr):
        if char=='X':
            left = min(left,i)
            right = max(right,i)

for i in range(top,bottom+1):
    print(''.join(result[i][left:right+1]))