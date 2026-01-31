import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())

switchs = list(map(int,input().split()))

stus = int(input())

result = []
students = []


for _ in range(stus):
    a,b = map(int,input().split())
    students.append((a,b))

for v in students:
    #남자
    if v[0]==1:
        for i in range(v[1],len(switchs)+1,v[1]):
            if switchs[i-1]==0:
                switchs[i-1]=1
            else:
                switchs[i-1]=0
    #여자
    else:
        
        #기준점을 기준으로 양 옆을 조사해야 한다.
        std_idx = v[1]-1
        min_idx = std_idx
        max_idx = std_idx
        for i in range(1,len(switchs)):
            left = std_idx-i
            right = std_idx+i
            if left>=0 and right<=len(switchs)-1:
                if switchs[left]==switchs[right]:
                    min_idx = left
                    max_idx = right
                else:
                    break
        for i in range(min_idx,max_idx+1):
            if switchs[i]==1:
                switchs[i]=0
            else:
                switchs[i]=1            
                


count=0
for i,num in enumerate(switchs):
    print(switchs[i],end=' ')
    if (i + 1) % 20 == 0 or i==len(switchs)-1:
        print()
