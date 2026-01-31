import sys

from itertools import combinations

def input():
    return sys.stdin.readline().rstrip()


input_value = input()

#1. 각 괄호 쌍 찾기
#2. 각 괄호에 번호를 매긴다.
#3. 괄호 조합을 생성한다.
#4. 생성한 조합에 따라 문자열을 만든다.
#5. 출력한다.
expression = []
stack=[]
data = []
result = set()
#괄호 조합 생성
for i, char in enumerate(input_value):
    if char == '(':
        stack.append(i)
    elif char == ')':
        first_idx = stack.pop()
        data.append((first_idx,i))
    else:
        expression.append(char)

#괄호 제거할 인덱스 만들기
for i in range(1,len(data)+1):
    for comb in combinations(data,i):
        remove_idx = set()
        for pair in comb:
            remove_idx.add(pair[0])
            remove_idx.add(pair[1])
        #remove_idx를 검사하면서 출력한다.
        reseult=''
        for i in range(len(input_value)):
            if i not in remove_idx:
                reseult += ''.join(input_value[i])

        result.add(reseult)
for res in sorted(result):
    print(res)