import sys

def input():
    return sys.stdin.readline().rstrip()


#한 손씩
#키를 옮기는 시간은 좌표 거리만큼 걸린다.
#키를 누를때도 1의 시간이 걸린다.

fir_left, fir_right = input().split()

ans = input()

keyboard = [
    ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
    ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
    ['z', 'x', 'c', 'v', 'b', 'n', 'm']
]

# 왼손/오른손 키 구분
left_keys = set(['q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v'])
right_keys = set(['y', 'u', 'i', 'o', 'p', 'h', 'j', 'k', 'l', 'b', 'n', 'm'])

pos = {}
for i, row in enumerate(keyboard):
    for j, char in enumerate(row):
        pos[char] = (i, j)

# 현재 손 위치
left_pos = pos[fir_left]
right_pos = pos[fir_right]

# 총 시간
time = 0

for char in ans:
    target_pos = pos[char]
    # 왼손으로 치는 키
    if char in left_keys:
        distance = abs(left_pos[0] - target_pos[0]) + abs(left_pos[1] - target_pos[1])
        time += distance + 1
        left_pos = target_pos
    # 오른손으로 치는 키
    else:
        distance = abs(right_pos[0] - target_pos[0]) + abs(right_pos[1] - target_pos[1])
        time += distance + 1
        right_pos = target_pos

print(time)