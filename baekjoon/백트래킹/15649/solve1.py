import sys
def input():
  return sys.stdin.readline().rstrip()

#1부터 N까지의 자연수 중 중복없이 M개를 고른 수열 출력
N,M = map(int,input().split())
visited = [False]*(N+1)
result = []
def backtrack(depth):
  if depth==N or len(result)==M:
    print(' '.join(map(str,result)))
    return
  
  for i in range(1,N+1):
    if not visited[i]:
      visited[i]=True
      result.append(i)
      backtrack(depth+1)
      result.pop()
      visited[i]=False

backtrack(0)
