import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())

price = list(map(int,input().split()))

joon=seng = N

joon_stock = 0
seng_stock = 0
pls_days = 0
mns_days = 0
temp = (0,0)
for i in range(len(price)):
    if i>0:
            if price[i-1]>price[i]:
                mns_days+=1
                pls_days=0
            elif price[i-1]<price[i]:
                pls_days+=1
                mns_days=0
            else:
                mns_days=0
                pls_days=0

    if joon>=price[i]:
        buy_count = joon // price[i]
        joon_stock += buy_count
        joon -= buy_count * price[i]

    if mns_days >= 3:
        buy_count = seng // price[i]
        seng_stock += buy_count
        seng -= buy_count * price[i]

    if pls_days >= 3 and seng_stock > 0:
        seng += seng_stock * price[i]
        seng_stock = 0

seng_result = seng+seng_stock*price[-1]
joon_result = joon+joon_stock*price[-1]


if seng_result>joon_result:
    print('TIMING')
elif seng_result<joon_result:
    print('BNP')
else:
    print('SAMESAME')