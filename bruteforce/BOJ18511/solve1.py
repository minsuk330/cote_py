import sys
sys.setrecursionlimit(10000000)
def input():
    return sys.stdin.readline().rstrip()

#N보다 작거나 같은 자연수 중 집합 K의 원소로만 구성된 가장 큰 수를 출력해라

N,K = map(int,input().split())

numbers = list(map(int,input().split()))

ans = -1
def recur(current):
    if current>N:
        return
    
    global ans

    ans = max(ans,current)

    for num in numbers:
        recur(current*10+num)


for num in numbers:
    recur(num)
print(ans)