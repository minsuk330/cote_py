import sys

def input():
    return sys.stdin.readline().rstrip()

#듣지 못한 사람의 명단
#보지 못한 사람의 명단 주어짐
#이때 듣지도 보지도 못한 사람의 명단을 구하여라
#두 명단의 교집합을 구하면 되네

N,M = map(int,input().split())

not_hear = {}
not_see = {}
count = 0
result = []
for _ in range(N):
    name = input()
    not_hear[name] = 1

for _ in range(M):
    name = input()
    not_see[name]=1

for key,value in not_hear.items():
    if not_see.get(key,0)==1:
        result.append(key)
        count+=1

result.sort()

print(count)
for name in result:
    print(name)