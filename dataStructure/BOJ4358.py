import sys


#각 그루가 몇번 나왔는지 카운트 하고 
#이걸 나눈 값을 출력하면 되겠다.

data = {}

trees = set()
total = 0
for line in sys.stdin:
    tree = line.rstrip()
    total+=1

    if trees and tree in trees:
        data[tree] = data[tree]+1
    else:
        trees.add(tree)
        data[tree] = 1

for name in sorted(data.keys()):
    per = data[name]/total*100

    print(f"{name} {per:.4f}")
    
