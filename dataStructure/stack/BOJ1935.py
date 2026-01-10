import sys

from collections import deque

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
all = input()
number = []

for _ in range(N):
    number.append(int(input()))

new_input = []
sick = []
for char in all:
    if char.isalpha():
        idx = ord(char) - ord('A')
        new_input.append(number[idx])
        
    else:
        sick.append(char)
        new_input.append(char)
result = 0

num = []
while new_input:
    temp = new_input.pop(0)
    if temp in sick:
        b = num.pop()
        a = num.pop()
        if temp == '+':
            num.append(a + b)
        elif temp == '-':
            num.append(a - b)
        elif temp == '*':
            num.append(a * b)
        elif temp == '/':
            num.append(a / b)
    else:
        num.append(temp)

print(f"{num[0]:.2f}")