import sys

def input():
    return sys.stdin.readline().rstrip()
L = int(input())
r = 31
M = 1234567891
data = input()
result = 0
for i,char in enumerate(data):
    value = (ord(char)-96)*pow(31,i)

    result+=value

result = result%M

print(result)