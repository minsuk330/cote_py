import sys

def input():
    return sys.stdin.readline().rstrip()
duck_s = ['q','u','a','c','k']
sound = input()
#q가 나오는 것들을 새롭게 넣어준다.
#새로운 소리가 나왔을 때 이미 완성된 quack가 있으면 오리를 추가하지 않는다.
ducks = {}
duck_size = 0
duck_idx = 0
for char in sound:
    if char=='q':
        for k,v in ducks.items():
            if v==[]:
                ducks[k].append('q')
                break
        else:
            ducks[duck_idx] = ['q']
            duck_idx+=1
            duck_size+=1
    else:
        for key,arr in ducks.items():
            if char==duck_s[len(arr)]:
                arr.append(char)
                # k를 추가해서 완성되면 초기화
                if len(arr) == 5:
                    ducks[key] = []
                break
        else:
            duck_size = -1
            break
count = 0

for k,v in ducks.items():
    if v==[]:
        count+=1
    elif v!=[]:
        # 미완성 오리가 있음
        print(-1)
        exit()

if count==0 or duck_size==-1:
    print(-1)
else:
    print(duck_size)



                