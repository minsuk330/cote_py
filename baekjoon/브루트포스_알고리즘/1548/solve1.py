import sys
def input():
  return sys.stdin.readline().rstrip()

#x+y>z, x+z>y, y+z>x 이걸 만족해야 한다.
N = int(input())
numbers = list(map(int,input().split()))
numbers = sorted(numbers)

#길이가 N인 수열 B의 모든 원소가 삼각관계에 있으면 이 수열은 삼각 수열이다.
#수열 A가 주어진다. 이 수열에서 몇개의 원소를 빼서 이 수열로 삼각 수열을 만들려고 한다.
#이때의 최대 길이를 구하시오

def get_count(idx):
  for i in range(N):
    if i + 1 < N and i+1<idx:
      j = i + 1
      # 가장 작은 두 수      
      sm = numbers[i] + numbers[j]
      if sm > numbers[idx]:
        result.append(idx-i+1)
        break

result = []
if N <= 2:
  print(N)
else:
  #현재는 가장 큰 수를 기준으로 뽑고있다.
  for i in range(N-1,1,-1):
    get_count(i)
  if not result:
    print(2)
  else:
    print(max(result))