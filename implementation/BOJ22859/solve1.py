import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

s = input()
result = ''
stack = deque()
tf = False
tag = ['div ','main']
temp_s = ''
title_s = ''
title_tf = False
for char in s:
    if char=='<':
        tf=True
        continue
    elif char=='>':
        tf==False
        continue
    
    if tf==True:
        if char=='=':
            continue
        elif char=='"':
            title_tf=True
            continue
        else:
            temp_s+=char

    if title_tf==True:
        if char=='"':
            title_tf=False
            if temp_s=='title':
                result+='title : '
                temp_s=''
            
        else:
            title_s+=char
    if temp_s in tag:
        temp_s=''
        

print(result)