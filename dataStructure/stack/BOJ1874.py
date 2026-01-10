import sys

def input():
    return sys.stdin.readline().rstrip()

#push하는 순서는 반드시 오름차순
#임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지, 
#있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지를 알아낼 수 있다.
#이를 계산하는 프로그램을 작성하라.

N = int(input())

input_stack = []
result = []
for _ in range(N):
    input_stack.append(int(input()))

result_stack = []
num = 1
for _ in range(N):
    input_front = input_stack.pop(0)
    while input_front>=num:
        result_stack.append(num)
        result.append('+')
        num+=1
    if input_front<num:
        if input_front==result_stack.pop():
            result.append('-')
        else:
            print('NO')
            break
else:
    for num in result:
        print(num)





    
        

        
