import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())

def round_up(avg):
    if avg>=0:
        result = int(avg+0.5)
        print(int(result))
    else:
        result = int(avg-0.5)
        print(int(result))
numbers = []
index = {}
for _ in range(N):
    data = int(input())
    numbers.append(data)
    index[data] = index.get(data,0)+1
total = sum(numbers)
#산술 평균
avg = total/N
round_up(avg)

#중앙 값
print(sorted(numbers)[N//2])
temp = []
#최빈값
#가장 많이 나온 수 추출해야 함
#만약 count가 같다면 2번째로 작은 수를 출력 해야 함
temp_value = 0
for key,value in sorted(index.items(),key=lambda x:x[1],reverse=True):
    if temp_value==0:
        temp_value = value
        temp.append(key)
    elif value==temp_value:
        temp.append(key)
if len(temp)>=2:
    temp.sort()
    print(temp[1])
else:
    print(temp[0])

print(max(numbers)-min(numbers))

    






