import sys
def input():
  return sys.stdin.readline().rstrip()

#두 문자열 S와 T가 있다면 S를 T로 바꾸는 게임
#연산1 문자열 뒤에 A를 추가한다
#역으로는 문자열 뒤에 A를 제거한다
#연산2 문자열 뒤에 B를 추가하고 뒤집는다.
#첫번째가 B라면 B를 제거하고 뒤집는다.

S = input()
T = input()
def dfs(t):
  if t==S:
    return 1
  if len(t)<=len(S):
    return 0
  
  result = 0

  if t[-1]=='A':
    result |=dfs(t[:-1])
  if t[0]=='B':
    result |=dfs(t[1:][::-1])

  return result

res = dfs(T)
print(res)
  