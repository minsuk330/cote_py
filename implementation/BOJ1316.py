import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
result = 0
for _ in range(N):
    check = []
    line=input()
    for i,char in enumerate(line):
        if char not in check:
            check.append(char)
        else:
            if line[i-1]!=char:
                break
    else:
        result+=1

print(result)