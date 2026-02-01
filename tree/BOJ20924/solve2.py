import sys

def input():
    return sys.stdin.readline().rstrip()
sys.setrecursionlimit(100000)


def tree_length(node,length,parent):
    #트리의 시작노드부터
    childs = []
    for child_node,value in tree[node]:
        if child_node!=parent:
            childs.append((child_node,value))

    if len(childs)==0:
        return (length,node,parent)
    elif len(childs)>=2:
        return (length,node,parent)
    else:
        return tree_length(childs[0][0],length+childs[0][1],node)
    

#트리에서 한 점에서의 최장거리
#해당 함수는 한 점이 주어지면 stack에 할당
def max_branch(start,parent):
    stack = [(start,parent,0)]
    branch_max = 0
    while stack:
        node,p,length = stack.pop()
        branch_max = max(branch_max,length)
        for next,w in tree[node]:
            if next!=p:
                stack.append((next,node,length+w))
    return branch_max
        
        

N,R = map(int,input().split())

tree = {i:[] for i in range(1,N+1)} 
parent = {}
for _ in range(N-1):
    a,b,d = map(int,input().split()) #a,b연결 d는 길이
    parent[b] = a #key의 부모는 value
    tree[a].append((b,d))
    tree[b].append((a,d))

length,giga,giga_parent=tree_length(R,0,-1)

gaji = max_branch(giga,giga_parent,0)#기가 노드부터 시작하면 되겠다.

print(length,gaji)