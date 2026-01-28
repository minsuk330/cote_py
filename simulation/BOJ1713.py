import sys

def input():
    return sys.stdin.readline().rstrip()

#최종 후보가 누구인지 결정해라
N = int(input())
M = int(input())
hoo = {}#여기엔 학생 번호와 추천 횟수를 같이 입력해준다.
result = [] 
numbers = list(map(int,input().split()))

for i,num in enumerate(numbers):
    if len(hoo)<N:
        hoo[num] = hoo.get(num,0)+1
    else:
        if num in hoo.keys():
            hoo[num] = hoo.get(num,0)+1
            continue
        min_value = 2000
        #가장 value가 적은 num찾아야 하고
        for key,value in hoo.items():
            min_value = min(min_value,value)
        #해당 value인 걸 dict에서 for로 찾아서 제거한다
        for key,value in hoo.items():
            if value==min_value:
                del hoo[key]
                break
        hoo[num] = hoo.get(num,0)+1

print(' '.join(map(str,sorted(hoo))))
