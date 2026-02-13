import sys,math
def input():
  return sys.stdin.readline().rstrip()

#N행 M열의 표 A가 있다.
#서로다른 칸 선택 행의 번호가 등차수열 이뤄야 하고 열의 번호도 등차수열을 이뤄야 한다.
#만들 수 있는 정수중 가장 큰 완전 제곱 수를 구하자
def is_square(n):
  r = math.isqrt(n)
  return r*r==n

def mk_number(i,j,dr,dc):
  nums = []
  s = ""
  while 0<=i<N and 0<=j<M:
    s+=board[i][j]
    nums.append(int(s))
    i+=dr
    j+=dc
  return nums


numbers = []

N,M = map(int,input().split())
board = []
for _ in range(N):
  line = list(input())
  board.append(line)

for i in range(N):
  for j in range(M):
    for dr in range(-N+1,N):
      for dc in range(-M+1,M):
        if dr==0 and dc==0:
          numbers.append(int(board[i][j]))
          continue
        numbers.extend(mk_number(i,j,dr,dc))

#numbers에 있는 수들 검사
numbers = [num for num in numbers if is_square(num)]
print(max(numbers) if numbers else -1)

