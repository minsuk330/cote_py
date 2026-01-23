import sys

def input():
    return sys.stdin.readline().rstrip()


#1과2와3의 합으로 수를 나타내는 경우의 수

T = int(input())
dp = [0]*12
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(12):
    if i>3:
        dp[i] = dp[i-1]+dp[i-2]+dp[i-3]


for _ in range(T):
    N = int(input())
    print(dp[N])

    