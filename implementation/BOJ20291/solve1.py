import sys

def input():
    return sys.stdin.readline().rstrip()

#확장자 별로 몇개 있는지?
#확장자를 사전순으로 정렬하기

n = int(input())
arr = []
check = {}
for _ in range(n):
    line = input()
    f=False
    temp = ''
    for char in line:
        if char=='.':
            f=True
            continue
        if f:
            temp+=char
    arr.append(temp)
arr.sort()

for s in arr:
    if check.get(s,0)==0:
        check[s]=1
    else:
        check[s]+=1

for key, value in check.items():
    print(f"{key} {value}")