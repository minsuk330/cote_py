import sys

def input():
    return sys.stdin.readline().rstrip()

numbers = {i:0 for i in range(1,31)}


for _ in range(28):
    num = int(input())
    numbers[num] = 1

result = []

for key,values in numbers.items():
    if values==0:
        result.append(key)

result.sort()

for i in result:
    print(i)
