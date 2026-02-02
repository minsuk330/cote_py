import sys

def input():
    return sys.stdin.readline().rstrip()


#N종류의 아이스크림이 있다.
#M은 섞어 먹으면 안되는 조합 수
N,M = map(int,input().split())
numbers = set()
for _ in range(M):
    a,b = map(int,input().split())
    numbers.add((a,b))
    numbers.add((b,a))
count = 0
for i in range(1,N+1):
    for j in range(i+1,N+1):
        for k in range(j+1,N+1):
            if (i,j) not in numbers and (i,k) not in numbers and (j,k) not in numbers:
                count+=1
print(count)
    