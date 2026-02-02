import sys

def input():
    return sys.stdin.readline().rstrip()


# N명이 치킨을 주문하려 함 M가지의 종류가 있다
# M가지 중 정확히 3가지를 선택
# 각 사람은 선택된 3가지 중 자신이 가장 선호하는 치킨의 만족도를 얻음
# 회원 만족도의 합이 최대가 되도록 한다.

N, M = map(int, input().split())
#각 사람 행 별로 선호도를 저장한다.
prefer = []
for _ in range(N):
    line = list(map(int, input().split()))
    prefer.append(line)
result = 0

for i in range(M):
    for j in range(i+1,M):
        for k in range(j+1,M):
            ##i,j,k는 치킨의 경우의 수
            total = 0
            for person in range(N):
                #각 사람별로 선호도 값 
                person_max = max(prefer[person][i], prefer[person][j], prefer[person][k])
                total+=person_max
            if total>=result:
                result=total

print(result)

            