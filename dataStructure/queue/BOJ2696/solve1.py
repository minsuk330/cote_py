import sys

def input():
    return sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    size = int(input())
    numbers = []
    result = []
    s=0
    if size%10==0:
        s=size//10
    else:
        s=size//10+1
    for _ in range(s):
        numbers += list(map(int,input().split()))
    temp = []
    for i,num in enumerate(numbers):
        temp.append(num)
        temp.sort()
        #이때마다 중앙 값 출력해야 한다.
        if i%2==0:
            result.append(temp[i//2])
    count=0
    print(len(result))
    for i, val in enumerate(result):
        if (i+1) %10==0:
            print(val)
        else:
            print(val,end=' ')
    print()

