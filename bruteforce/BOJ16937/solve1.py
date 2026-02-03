import sys

def input():
    return sys.stdin.readline().strip()

#크기 HW이고 N개의 스티커
#스티커의 크기는 R*C이다
#모눈종이에 스티커 2개를 붙이려 한다. 스티커 90도 회전 가능
#스티커는 접하기만 가능하고 

#두 스티커가 붙여진 넓이의 최대 값을 구하라


H,W = map(int,input().split())
max_results = []

N = int(input())
sticker = []

for i in range(N):
    r,c = map(int,input().split())
    sticker.append((r,c))
comb = [] #가능한 모든 조합 넣어두기
for i in range(N):
    for j in range(i+1,N):
        comb.append((i,j))

for i,j in comb:
    fr,fc = sticker[i][0],sticker[i][1]
    sr,sc = sticker[j][0],sticker[j][1]
    r_max = max(fr,sr)
    c_max = max(fc,sc)
        #둘 중에 기준을 하나 잡고 거기에 나란히 맞추게 하기
        #두 스티커를 가로로 배치
        #정렬 없이
    if fr+sr<=H and max(fc,sc)<=W:
        max_results.append(fr*fc+sr*sc)
    #첫번째를 90도 회전
    elif fc+sr<=H and max(fr,sc)<=W:
        max_results.append(fr*fc+sr*sc)
    #두번째를 90도 회전
    elif fr+sc<=H and max(fc,sr)<=W:
        max_results.append(fr*fc+sr*sc)
    elif fc+sc<=H and max(fr,sr)<=W:
        max_results.append(fr*fc+sr*sc)

    #두 스티커를 세로로 배치
    elif max(fr,sr)<=H and fc+sc<=W:
        max_results.append(fr*fc+sr*sc)
    elif max(fc,sr)<=H and fr+sc<=W:
        max_results.append(fr*fc+sr*sc)
    elif max(fr,sc)<=H and fc+sr<=W:
        max_results.append(fr*fc+sr*sc)
    elif max(fc,sc)<=H and fr+sr<=W:
        max_results.append(fr*fc+sr*sc)
if max_results:
    print(max(max_results))
else:
    print(0)