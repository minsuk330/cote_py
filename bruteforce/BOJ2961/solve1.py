import sys
from itertools import combinations
def input():
    return sys.stdin.readline().rstrip()

#재료 N개 존재
#신 쓴 맛을 알 고 있다. 재료를 섞어 둘의 차이를 적게 만들려 한다.
#신맛은 사용한 재료의 곱이고 쓴맛은 합이다.
#이때 둘의 차이를 최소로 하는 것을 계산해라

N = int(input())
ingre = []
for i in range(N):
    S,B = map(int,input().split())
    ingre.append((S,B))

#재료가 1~N개별로 각 조합의 최소값을 구하면 될려나?
min_diff = float('inf')

for count in range(1, N+1):
    # count개의 재료를 선택하는 모든 조합
    for comb in combinations(ingre,count):
        sour = 1
        bitter = 0

        for s,b in comb:
            sour*=s
            bitter+=b

        value = abs(sour-bitter)
        min_diff = min(value,min_diff)

print(min_diff)