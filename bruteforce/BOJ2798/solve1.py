import sys

def input():
    return sys.stdin.readline().rstrip()


#카드의 합이 21넘지 않고 카드의 합을 최대 크게

#N장의 카드를 바닥에 놓는다. 이후 딜러는M 외침
#제한시간 안에 카드 3장 고르기 M과 최대한 가깝게

#이건 걍 for3개 돌리면 되는거 아닌가

N,M = map(int,input().split())

cards = list(map(int,input().split()))
result = []
min_cards = M+1
for i in range(N):
    for j in range(i,N):
        for k in range(j,N):
            if i!=j and j!=k and k!=i:

                if cards[i]+cards[j]+cards[k]<=M:
                    result.append(cards[i]+cards[j]+cards[k])      
result.sort()
print(result[-1])
                
