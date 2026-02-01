import sys

def input():
    return sys.stdin.readline().rstrip()

N,K = map(int,input().split())

#00시00분00초 부터 N시 59분59초까지 모든 시각중
#K가 하나라도 포함되는 모든 시각을 
count = 0

#hh->mm->ss 이거 순으로 증가하게 만들자

for h in range(N+1):
    for m in range(60):
        for s in range(60):
            st = f"{h:02d}{m:02d}{s:02d}"
            if str(K) in st:
                count+=1

print(count)
            
