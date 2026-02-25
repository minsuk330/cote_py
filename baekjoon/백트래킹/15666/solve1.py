import sys
def input():
  return sys.stdin.readline().rstrip()

N,M = map(int,input().split())
numbers = list(map(int,input().split()))
numbers.sort()
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
    if result and result[-1]<=num:
      result.append(num)
      backtrack(depth+1)
      result.pop()
    elif not result:
      result.append(num)
      backtrack(depth+1)
      result.pop()

backtrack(0)