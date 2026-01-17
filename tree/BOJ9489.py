import sys

from collections import deque

def input():
    return sys.stdin.readline().rstrip()
    
while True:
    node_count,node_number = map(int,input().split())
    if node_count==0 and node_number==0:
        break
    parent = {}
    numbers = list(map(int,input().split()))
    tree = {i:[] for i in numbers}
    
    root = 0
    level = 0
    for i,num in enumerate(numbers):
        if i==0:
            root = num
            parent[root] = None
            continue
        if i==1:
            tree[numbers[level]].append(num)
            parent[num] = numbers[level]
        else:
            if tree[numbers[level]][-1]+1==num:   
                tree[numbers[level]].append(num)
                parent[num] = numbers[level]
            else:
                level+=1
                tree[numbers[level]].append(num)
                parent[num] = numbers[level]
    
    target_parent = parent.get(node_number,None)
    if target_parent is None:
        print(0)
        continue
    
    target_grandparent = parent.get(target_parent,None)
    if target_grandparent is None:
        print(0)
        continue

    count = 0
    
    for node in numbers:
        if node == node_number:
            continue
        node_parent = parent.get(node,None)
        
        if node_parent is None:
            continue
        if node_parent == target_parent:
            continue
        node_grandparent = parent.get(node_parent, None)
        if node_grandparent == target_grandparent:
            count += 1

    print(count)
