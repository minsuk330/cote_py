import sys

def input():
    return sys.stdin.readline().rstrip()

def tree_length(node, value, parent):
    childs = []
    for child, length in tree[node]:
        if child != parent:
            childs.append((child, length))
    
    if len(childs) == 0:
        return (value, node, parent)
    elif len(childs) >= 2:
        return (value, node, parent)
    else:
        next, length = childs[0]
        return tree_length(next, length+value, node)
    
def max_branch(node,cur_length,parent):
    childs = []
    for child,length in tree[node]:
        if child !=parent:
            childs.append((child,length))

    #리프인 경우
    if len(childs)==0:
        return cur_length
    
    max_length = 0
    for child,value in childs:
        branch_length = max_branch(child,value+cur_length,node)
        max_length = max(max_length,branch_length)

    return max_length
        

parent = {}
node_count,root =map(int,input().split())
tree = {i:[]for i in range(1,node_count+1)}

for _ in range(node_count-1):
    node1,node2,length = map(int,input().split())
    #해당 노드의 자식 노드가 몇 개인지? -> dfs로 구하고
    #가지의 길이 찾은 기가 노드와 리프 노드간 간선 길이
    parent[node2] = node1
    tree[node1].append((node2,length))
    tree[node2].append((node1,length))

#이제 기둥의 길이를 찾자

length, giga, giga_parent = tree_length(root, 0, -1)
branch = max_branch(giga, 0, giga_parent)
print(f"{length} {branch}")
