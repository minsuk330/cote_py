# BOJ 14501 - 퇴사

## 문제 링크
https://www.acmicpc.net/problem/14501

## 문제 요약
- N일 후 퇴사를 앞두고 있음
- 각 날짜마다 상담이 하나씩 잡혀있음 (소요 기간 T, 금액 P)
- 상담은 T일이 걸리며, 퇴사일 이전에 끝나야 함
- 겹치지 않게 상담을 선택하여 최대 수익 구하기

## 접근 방법

### 1. 브루트포스 (DFS - 선택/비선택)
- 각 날짜의 상담에 대해 "선택함/선택 안 함" 두 가지 경우 탐색
- BOJ 16508과 동일한 부분집합 탐색 패턴
- 시간복잡도: O(2^n)

### 2. 핵심 로직
```python
def dfs(idx, price):
    # 1. 모든 날짜 확인 완료 → max_price 갱신
    if idx >= N:
        max_price = max(max_price, price)
        return

    # 2. 선택 안 함: 다음 날로 이동
    dfs(idx + 1, price)

    # 3. 선택함: 상담이 끝나는 날로 이동
    time, s_price = schedule[idx]
    if idx + time <= N:  # 퇴사일 내에 끝나는지 확인
        dfs(idx + time, price + s_price)
```


## 다른 풀이
- dp로 풀어봐야 한다.

## 시간복잡도
- DFS: O(2^n)
- DP: O(n)

## 공간복잡도
- DFS: O(n) - 재귀 깊이
- DP: O(n) - dp 배열
