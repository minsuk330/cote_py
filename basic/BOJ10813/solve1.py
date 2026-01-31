N,M = map(int,input().split())

arr = []

for i in range(N):
    arr.append(i+1)

for _ in range(M):
    a,b = map(int,input().split())
    temp = 0
    temp = arr[a-1]
    arr[a-1] = arr[b-1]
    arr[b-1] = temp

print(' '.join(map(str,arr)))