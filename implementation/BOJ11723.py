import sys

def input():
    return sys.stdin.readline().rstrip()


M = int(input())

arr = set()

for _ in range(M):
    cmds = list(map(str,input().split()))
    if len(cmds)==2:
        num_int = int(cmds[1])
    cmd = cmds[0]

    if cmd=='add':
        if num_int in arr:
            continue
        else:
            arr.add(num_int)
    elif cmd=='check':
        if num_int in arr:
            print(1)
        else:
            print(0)
    elif cmd=='remove':
        if num_int in arr:
            arr.remove(num_int)
        else:
            continue
    elif cmd=='toggle':
        if num_int in arr:
            arr.remove(num_int)
        else:
            arr.add(num_int)

    elif cmd=='all':
        temp = set()
        for i in range(20):
            temp.add(i+1)
        arr = temp

    else:
        arr.clear()
