# BOJ 14620 - 꽃길

## 문제 정보
- **문제 번호**: 14620
- **문제 이름**: 꽃길
- **난이도**: Silver 2
- **분류**: 브루트포스, 백트래킹
- **링크**: https://www.acmicpc.net/problem/14620

## 문제 설명
N×N 크기의 화단에 꽃 3개를 심으려고 한다. 꽃을 심으면 중심과 상하좌우 4방향으로 꽃잎이 펴지므로, 한 꽃당 총 5칸을 차지한다.

### 제약 조건
1. 꽃잎이 화단 밖으로 나가면 안 된다
2. 꽃잎끼리 겹치면 안 된다
3. 각 칸마다 비용이 다르며, 꽃이 차지하는 5칸의 비용 합을 최소화해야 한다

### 입력
- 첫째 줄: N (6 ≤ N ≤ 10)
- 둘째 줄부터 N개 줄: 각 칸의 비용 (0 ≤ 비용 ≤ 200)

### 출력
- 꽃 3개를 심는 최소 비용

## 핵심 알고리즘: 백트래킹 (Backtracking)

### 백트래킹이란?
**모든 경우의 수를 탐색하되, 불가능한 경우는 일찍 포기하는 알고리즘**

```
선택 → 탐색 → 취소 (되돌아가기) → 다음 선택
```

### 백트래킹의 핵심 패턴
```python
def backtrack(상태):
    if 목표_달성:
        return 결과

    for 선택 in 선택지들:
        if 선택_가능():
            선택_적용()          # 1. 선택
            backtrack(다음_상태)  # 2. 탐색
            선택_취소()          # 3. 되돌리기 ⭐
```

### 왜 선택을 취소해야 하나?
선택을 취소하지 않으면 다른 조합을 시도할 수 없다!

```
[A 선택] → [B 선택] → [C 선택] ✓ 결과1
                    ← [C 취소]  ⭐ 안 하면 D를 못 선택!
                    → [D 선택] ✓ 결과2
```

## 풀이 전략

### 1. 전처리: 가능한 꽃 위치 찾기
```python
board_price = []  # (i, j, 비용) 저장

for i in range(N):
    for j in range(N):
        # 중심이 테두리가 아닌 경우만 (상하좌우가 범위 안에 있어야 함)
        if 0 < i < N-1 and 0 < j < N-1:
            # 중심 + 상하좌우 비용 계산
            price = board[i][j]
            for di, dj in [(1,0),(-1,0),(0,1),(0,-1)]:
                price += board[i+di][j+dj]
            board_price.append((i, j, price))
```

### 2. 백트래킹으로 3개 선택
```python
visited = [[False] * N for _ in range(N)]  # 방문 체크 배열

def dfs(idx, count, total_cost):
    # 종료 조건: 3개 선택 완료
    if count == 3:
        return total_cost

    min_cost = float('inf')

    # idx부터 끝까지 탐색 (중복 방지)
    for k in range(idx, len(board_price)):
        i, j, price = board_price[k]

        # 가지치기: 배치 불가능하면 스킵
        if can_place(i, j):
            place_flower(i, j)    # 1. 선택
            result = dfs(k+1, count+1, total_cost+price)  # 2. 재귀
            min_cost = min(min_cost, result)
            remove_flower(i, j)   # 3. 취소 (백트래킹!)

    return min_cost
```

### 3. 보조 함수

#### can_place(i, j): 배치 가능 여부 확인
```python
def can_place(i, j):
    if visited[i][j]:  # 중심이 사용 중
        return False
    for di, dj in direc:
        if visited[i+di][j+dj]:  # 꽃잎이 사용 중
            return False
    return True
```

#### place_flower(i, j): 꽃 심기
```python
def place_flower(i, j):
    visited[i][j] = True
    for di, dj in direc:
        visited[i+di][j+dj] = True
```

#### remove_flower(i, j): 꽃 제거
```python
def remove_flower(i, j):
    visited[i][j] = False
    for di, dj in direc:
        visited[i+di][j+dj] = False
```

## 실행 흐름 예시

```
board_price = [(1,1,10), (1,3,15), (3,1,12), (3,3,8)]

dfs(0, 0, 0)
├─ (1,1) 선택 ✓ visited[1][1] = True
│  └─ dfs(1, 1, 10)
│     ├─ (1,3) 선택 ✓ visited[1][3] = True
│     │  └─ dfs(2, 2, 25)
│     │     └─ (3,1) 선택 ✓ count==3 → return 37
│     │     └─ (3,1) 취소 ✗
│     ├─ (1,3) 취소 ✗ visited[1][3] = False
│     └─ (3,1) 선택 ✓ ...
└─ (1,1) 취소 ✗ visited[1][1] = False
```

## 시간 복잡도
- 가능한 꽃 위치: 최대 (N-2)² ≈ 64개 (N=10일 때)
- 3개 선택: C(64, 3) ≈ 41,000
- 각 선택마다 충돌 체크: O(1)
- **총 시간복잡도**: O(N² × C(N², 3)) → 충분히 통과

## 핵심 포인트
1. **전처리**: 가능한 위치를 미리 계산해서 탐색 공간 축소
2. **visited 배열**: 꽃이 차지하는 5칸을 모두 체크
3. **백트래킹**: `place_flower` → 재귀 → `remove_flower` 패턴
4. **가지치기**: `can_place`로 불가능한 경우 조기 차단

## 실수하기 쉬운 부분
1. `min_cost = (min_cost, result)` → 튜플이 됨! `min()` 사용해야 함
2. `remove_flower()` 누락 → 백트래킹이 안 돼서 다른 조합 탐색 불가
3. `visited` 초기화를 `dfs()` 호출 전에 해야 함
4. 테두리 체크: 중심이 `0 < i < N-1` 범위에 있어야 함

## 참고
- [solve1.py](solve1.py): 백트래킹 풀이
