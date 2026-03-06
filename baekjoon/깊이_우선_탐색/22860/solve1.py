import sys

sys.setrecursionlimit(100000)
def input():
  return sys.stdin.readline().rstrip()

##Folder는 폴더 file은 파일

#한 폴더 안에는 같은 이름 파일 존재할 수 없다
#main 하위 디렉토리에 같은 이름 폴더가 두 개 이상 존재할 수 없다.
#N은 폴더의 총 개수 M은 파일의 총 개수

#타겟 하위에 있는 모든 파일을 가져와야 한다.
def dfs(target):
  global files1
  global files2
  
  nexts = tree.get(target, [])
  for f,c in nexts:
    #폴더인 경우
    if c==1:
      #더 깊이 탐색 해야 함
      dfs(f)
    #파일인 경우
    else:
      if f not in files1:
        files1.append(f)
      files2.append(f)
  

N,M = map(int,input().split())
tree = dict()
for _ in range(N+M):
  #p는 상위폴더 f는 폴더 또는 파일 이름, c는 폴더인지 아닌지 알려줌
  #c는 1이면 폴더 0이면 파일
  P,F,C = input().split()
  C = int(C)
  if P in tree:
    tree[P].append((F,C))
  else:
    tree[P] = [(F,C)]
query = int(input())

for _ in range(query):
#   #쿼리 순서대로 . 한줄. ㅣㄱ 하위의 있는 파일 종류의 개수와 파일 . 총개수를 구하여라
  line = list(input().split('/'))
  last_folder = line[-1]
  files1 = []
  files2 = []
  dfs(last_folder)
  print(len(files1), len(files2))

