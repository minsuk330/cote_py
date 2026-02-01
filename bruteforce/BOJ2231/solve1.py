import sys

def input():
    return sys.stdin.readline().rstrip()
#분해합->각 자릿수의 함
#어떤 자연수 M의 분해합이 N이면 M은 N의 생성자인다.


N = int(input())

#가장 작은 생성자를 출력하라
result = 0
for i in range(N):
    temp = i
    num = i
    while num>=1:
        temp+=num%10
        num = num//10
    if temp==N:
        print(i)
        break
else:
    print(0)