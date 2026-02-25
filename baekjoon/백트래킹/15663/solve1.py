import sys
def input():
  return sys.stdin.readline().rstrip()

N,M = map(int,input().split())
numbers = list(map(int,input().split()))
numbers.sort()
visited = [False]*(N+1)
index = set()
result = []
#1~N까지의 수열 같은수를 여러번 골라도 된다. 증가하는 순으로 작성

def backtrack(depth):
  if depth==N or len(result)==M:
    if tuple(result) not in index:
      index.add(tuple(result))
      print(' '.join(map(str,result)))
    return

  for i,num in enumerate(numbers):
    if not visited[i]:
      visited[i] = True
      result.append(num)
      backtrack(depth+1)
      visited[i] = False
      result.pop()

backtrack(0)