import sys
def input(): return sys.stdin.readline().rstrip()

N, M, R = map(int, input().split())
dir = {'E': (0, 1), 'W': (0, -1), 'S': (1, 0), 'N': (-1, 0)}  # (dy, dx)

board = [list(map(int, input().split())) for _ in range(N)]
check = [['S'] * M for _ in range(N)]

score = 0

for _ in range(R):
    X, Y, D = input().split()
    r = int(X) - 1
    c = int(Y) - 1
    dy, dx = dir[D]

    if check[r][c] == 'S':
        rem = board[r][c]
        nr, nc = r, c

        while rem > 0 and 0 <= nr < N and 0 <= nc < M:
            if check[nr][nc] == 'S':
                check[nr][nc] = 'F'
                score += 1
                rem = max(rem, board[nr][nc])  # 더 긴 도미노 만나면 확장
            rem -= 1
            nr += dy
            nc += dx

    X, Y = map(int, input().split())
    r = X - 1
    c = Y - 1
    check[r][c] = 'S'

print(score)
for i in range(N):
    print(' '.join(check[i]))