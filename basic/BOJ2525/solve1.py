a,b = map(int,input().split())
c = int(input())

total_minuite = a*60 + b + c

hour = total_minuite//60

minute = total_minuite%60


if hour >= 24 :
    hour = hour%24

print(f"{hour} {minute}")
