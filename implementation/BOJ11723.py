import sys

def input():
    return sys.stdin.readline().rstrip()


M = int(input())

arr = set()

for _ in range(M):
    cmds = input().split()
    cmd = cmds[0]

    if cmd=='add':
        arr.add(int(cmds[1]))
    elif cmd=='check':
        if int(cmds[1]) in arr:
            print(1)
        else:
            print(0)
    elif cmd=='remove':
        if int(cmds[1]) in arr:
            arr.remove(int(cmds[1]))
        else:
            continue
    elif cmd=='toggle':
        if int(cmds[1]) in arr:
            arr.remove(int(cmds[1]))
        else:
            arr.add(int(cmds[1]))

    elif cmd=='all':
        arr = set(range(1,21))

    else:
        arr.clear()
