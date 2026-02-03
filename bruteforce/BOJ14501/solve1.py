import sys

def input():
    return sys.stdin.readline().rstrip()

#오늘부터 n+1째 되는 날 퇴사를 하려고 한다.
#남은 N일 동안 최대한 많은 상담을 하려고 함
#하루에 하나씩 서로 다른 상담을 잡아 놓는다.

#상담에 걸리는 기간 T, 금색 p

#문제 자체가 뉘앙스가 해당 조건을 걸고
#조건에 부합하는 최대와 최소 값을 찾아라
#이런건 전부 찾아야 한다.

def dfs(idx,price):
    global max_price
    #전부 탐색했다면 끝
    if idx>=N:
        max_price = max(max_price,price)
        return
    
    #선택하지 않는 경우
    dfs(idx+1,price)

    time,s_price = schedule[idx]

    if idx+time>N:
        max_price = max(max_price,price)
        return

    dfs(idx+time,s_price+price)


N = int(input())
schedule =[]
for i in range(N):
    time,price = map(int,input().split())
    schedule.append((time,price))

max_price=-1
dfs(0,0)

print(max_price)