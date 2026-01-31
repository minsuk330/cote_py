import sys

def input():
    return sys.stdin.readline().rstrip()

arr = []

for i in range(3):
    arr.append(input())
result = 0
idx = 0
for i,char in enumerate(arr):
    if char.isdigit():
        idx = i
if idx==0:
    result = int(arr[idx])+3
elif idx==1:
    result = int(arr[idx])+2
else:
    result = int(arr[idx])+1

if result%3==0 and result%5==0:
    print("FizzBuzz")
elif result%3!=0 and result%5==0:
    print("Buzz")
elif result%3==0 and result%5!=0:
    print("Fizz")
else:
    print(result)

        
        