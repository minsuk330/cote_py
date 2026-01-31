import sys

def input():
    return sys.stdin.readline().rstrip()

#ISBN이 abcdefghijklm 일 때, a+3b+c+3d+e+3f+g+3h+i+3j+k+3l+m ≡ 0 (mod 10)

# m = 10 - (a+3b+c+3d+e+3f+g+3h+i+3j+k+3l) mod 10

data = input()
numbers = []
idx = 0
for i,char in enumerate(data):
    if char.isdigit():
        numbers.append(int(char))
    else:
        numbers.append('*')
        idx = i
total = 0
if numbers[12]=='*':
    for i,num in enumerate(numbers):
        if num!='*':
            if i%2==0:
                total+=num 
            else:
                total = total+num*3
    for i in range(10):
        if (total+i)%10==0:
            print(i)
            break
else:
    for i in range(13):
        num = numbers[i]
        if numbers[i]!='*':
            if i%2==0:
                total+=num       
            else:
                total = total+num*3

    for i in range(10):
        if idx%2==0:
            if (total+i)%10==0:
                print(i)
                break
        else:
            if (total+i*3)%10==0:
                print(i)
                break

    

    