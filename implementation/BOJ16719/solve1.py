import sys

def input():
    return sys.stdin.readline().rstrip()

#아직 보여주지 않은 문자 중 추가했을 때의 문자열이 사전순으로 가장 앞에 오도록
#문자열이 주어졌을때
#문자열 중에 가장 값이 적은 걸 추가하고 이후 해당 문자열 뒤에 붙인다
#이후 앞에 붙여야 할땐 

s = input()

arr = []
for i,char in enumerate(s):
    arr.append((char,i))

#문자 순으로 정렬이 되어 있다.
result = ['' for _ in range(len(arr))]
last_idx = 0
deleted_keys = []
print(sorted(arr))
for key,idx in (sorted(arr)):
    if result==[]:
        result.insert(idx,key)
        deleted_keys.append(key)
        last_idx = idx
        print(key)
        continue
    
    if idx>last_idx:
        result.insert(idx,key)
        deleted_keys.append(key)
        last_idx = idx
        print(''.join(result))

for key,idx in sorted(arr):
    if idx<last_idx:
        if key not in deleted_keys:
            result.insert(idx,key)
            print(''.join(result))
