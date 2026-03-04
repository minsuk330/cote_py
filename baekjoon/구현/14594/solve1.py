import sys
def input():
  return sys.stdin.readline().rstrip()

N = int(input())
M = int(input())
walls = [1]*(N-1)
for _ in range(M):
  x,y = map(int,input().split())
  if x<y:
    for i in range(x-1,y-1):

      walls[i]=0
    

print(sum(walls)+1)

