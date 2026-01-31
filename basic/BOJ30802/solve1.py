import sys

def input():
    return sys.stdin.readline().rstrip()


N = int(input())

shirts = list(map(int,input().split()))
#p는 펜의 묶음 수
#펜은 참가자 수 만큼만

#펜을 p자루씩 최대 몇 묶음 주문 가능한지, 
#그때 펜을 한자루 몇개 주문해야 하는지
T,P = map(int,input().split())

#펜은 정확하게
shirts_count = 0
for num in shirts:
    if num == 0:
        continue
    if num%T==0:
        shirts_count+=num//T
    else:
        shirts_count+=num//T+1

max_pen = N//P
one_pen = N%P

print(int(shirts_count))
print(int(max_pen), one_pen)
