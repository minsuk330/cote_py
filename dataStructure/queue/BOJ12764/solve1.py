import sys,heapq

def input():
    return sys.stdin.readline().rstrip()

#사람수
N = int(input())

#시작시간 종료시간

#모든 사람이 기다리지 않아도 되는 최소 값

#컴퓨터는 1번부터 착석한다.
computer = {} #key는 컴퓨터 번호, value는 count
people = []
use_computer = []#남은 시각과 컴퓨터 번호를 넣어두자
offset = 0
for _ in range(N):
    start,end = map(int,input().split())
    people.append((start,end))

people.sort()

seat = 0
available = []

for start, end in people:
    ##이미 지난 것들 넣어주고 
    offset = start
    while use_computer and use_computer[0][0]<=offset:
        end_time, seat_num = heapq.heappop(use_computer)
        heapq.heappush(available,seat_num)

    ##사용 가능 자리가 있을 경우
    if available:
        seat_num = heapq.heappop(available)
        computer[seat_num]+=1
        heapq.heappush(use_computer,(end,seat_num))
    else:
        seat+=1
        computer[seat] = computer.get(seat,0)+1
        heapq.heappush(use_computer,(end,seat))



print(seat)
# 자리 번호 순서대로 출력

for i in range(1,seat+1,1):
    print(computer[i], end=' ')
print()
            






    