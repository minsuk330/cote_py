import sys
def input():
  return sys.stdin.readline().rstrip()

N,M = map(int,input().split())
result = []
#1~N까지의 수열 같은수를 여러번 골라도 된다. 증가하는 순으로 작성

def backtrack(depth):
  if depth==N or len(result)==M:
    print(' '.join(map(str,result)))
    return
  
  for i in range(1,N+1):
    result.append(i)
    backtrack(depth+1)
    result.pop()


backtrack(0)