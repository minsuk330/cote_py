import sys

def input():
    return sys.stdin.readline().rstrip()

#A,T,G,C
#길이가 같은 두 DNA가 있을 때 각 위치의 문자가 다른 것의 개수

#N개의 길이M인 DNA가 주어지면 HD의 합이 가장 작은 것을 구하는 것

#첫째줄에 HD의 합이 가장 작은걸 출력 둘째줄 그 HD의 합을 출력하라

N,M = map(int,input().split())
#각 인덱스의 문자가 몇번 나왔는지 체크를 해야 한다.

check = {i:[]for i in range(M)}
result = []
for _ in range(N):
    line = input()
    for i,char in enumerate(line):
        check[i].append(char)

for i in range(M):
    a,t,g,c = 0,0,0,0
    for char in check[i]:
        if char=='A':
            a+=1
        elif char=='T':
            t+=1
        elif char=='G':
            g+=1
        else:
            c+=1
    #뭐가 가장 큰지에 따라 정하면 된다.
    max_count = max(a,t,g,c)
    if a == max_count:
        result.append('A')
    elif c == max_count:
        result.append('C')
    elif g == max_count:
        result.append('G')
    else:
        result.append('T')

hd_sum = 0
for i in range(M):
    for char in check[i]:
        if char != result[i]:
            hd_sum += 1

print(''.join(result))
print(hd_sum)