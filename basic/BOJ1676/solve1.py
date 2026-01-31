import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())

calc = 1
for i in range(N):
    calc *=(i+1)

str_cal = str(calc)
stack = []
count = 0
for num in str_cal:
    stack.append(int(num))

for _ in range(len(stack)):
    if stack.pop()==0:
        count+=1
    else:
        break

print(count)