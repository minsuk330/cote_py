import sys

def input():
    return sys.stdin.readline().rstrip()

target = input()

n = int(input())

books = []

def dfs(idx, char_check, cur_price):
    global min_price

    #모든 char_check를 다썼다면
    if all(cnt<=0 for cnt in char_check.values()):  
        min_price = min(min_price,cur_price)
        return
    if idx>=n:
        return
    
    if cur_price>=min_price:
        return
    
    #선택을 안할 경우
    dfs(idx+1,char_check,cur_price)

    new_check = dict(char_check)
    price,name = books[idx]

    for char in name:
        if char in new_check:
            new_check[char]-=1
    
    dfs(idx+1,new_check,cur_price+price)

#단어 체크 용도
#각 단어의 개수를 체크 해야 한다.
char_check={}

min_price = float('inf')
for char in target:
    char_check[char] = char_check.get(char,0)+1


for _ in range(n):
    price,name = map(str,input().split())
    books.append((int(price),name))

dfs(0, char_check, 0)

if min_price == float('inf'):
    print(-1)
else:
    print(min_price)
