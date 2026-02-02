import sys

def input():
    return sys.stdin.readline().rstrip()

#n장의 카드 중 k장을 선택하고 정수를 만든다.
#이때 만들 수 있는 정수의 수는 몇개인가?

def recur(k,char,visited):
    if k==0:
        result.add(char)
        return
    for i in range(len(cards)):
        if not visited[i]:
            visited[i]=True
            recur(k-1,char+cards[i],visited)
            visited[i]=False


n = int(input())
visited = [False]*n
k = int(input())
cards = []
result = set()
for i in range(n):
    card = int(input())
    cards.append(str(card))
recur(k,'',visited)
print(len(result))
    
    