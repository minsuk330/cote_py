import sys

def input():
    return sys.stdin.readline().rstrip()

N,M,R = map(int,input().split())

layers = min(N,M)//2

arr = [[] for _ in range(N)]

for i in range(N):
    arr[i] = list(map(int,input().split()))

for layer in range(layers):
    temp = []

    #첫줄 왼->오
    for j in range(layer,M-layer):
        temp.append(arr[layer][j])
    #오른쪽 위->아래
    for j in range(layer+1,N-layer):
        temp.append(arr[j][M-layer-1])
    #아래쪽
    for j in range(M-layer-2,layer-1,-1):
        temp.append(arr[N-layer-1][j])
    #왼쪽
    for i in range(N - layer - 2, layer, -1):
        temp.append(arr[i][layer])

    
    rotate_c = R%len(temp)

    temp = temp[rotate_c:] + temp[:rotate_c]
    idx = 0
    for j in range(layer,M-layer):
        arr[layer][j] = temp[idx]
        idx+=1
    #오른쪽 위->아래
    for j in range(layer+1,N-layer):
        arr[j][M-layer-1] = temp[idx]
        idx+=1
    #아래쪽
    for j in range(M-layer-2,layer-1,-1):
        arr[N-layer-1][j]=temp[idx]
        idx+=1
    #왼쪽
    for i in range(N - layer - 2, layer, -1):
        arr[i][layer] = temp[idx]
        idx+=1

for i in range(N):
    for j in range(M):
        print(arr[i][j],end=' ')
    print()

    
    



