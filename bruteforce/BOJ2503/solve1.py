import sys

def input():
    return sys.stdin.readline().rstrip()

##영수 1~9까지 서로다른 숫자 세개로 수정된 세자리 수를 생각
#민혁이는 1~9까지 서로다른 세자리수 영수에게 묻는다
#만약 민혁이 물은 세자리 수중 하나가 영수의 수에 동일한 자리에 위치하면 스트라이크, 숫자가 있기만하면 볼이다.

#민혁이가 영수의 세자리수를 정확하게 밪춰 3 스트라이크가 되면 게임 셋 아니라면 계속 새로운 수를 생각해내야 한다.
#현재 게임도중이다.
#민혁이가 영수에게 어떤 수를 물어봤는지 그리고 각각의 물음에 어떻게 답했는지 입력으로 주어진다.
#이를 통해 난 가능성이 있는 수가 총 몇개인지 맞춰야 한다.

n = int(input())
arr = []
result = 0
for i in range(n):
    num,strike,ball = map(int,input().split())
    arr.append((num,strike,ball))
for number in range(123,988):
    s = str(number)
    if '0' in s:
        continue

    if len(set(s))!=3:
        continue

    flg = True
    
    for num,strike,ball in arr:
        strike_count = 0
        ball_count = 0
        query = str(num)

        #스트라이크 체크
        for i in range(3):
            if s[i]==query[i]:
                strike_count+=1
        #볼 체크
        for i in range(3):
            if query[i] in s and query[i]!=s[i]:
                ball_count+=1

        if strike != strike_count or ball != ball_count:
            flg = False
            break
    if flg:
        result+=1

print(result)
    