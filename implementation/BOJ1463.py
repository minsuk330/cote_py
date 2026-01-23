import sys

def input():
    return sys.stdin.readline().rstrip()


N = int(input())

#3으로 나누면 3으로 나눔
#2로 나눠지면 2로 나눔
#1을 뺌


#이걸로 1을 만들어야 함
dp = [0]*(N+1)

for i in range(2,N+1):
    dp[i] = dp[i-1]+1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[N])
