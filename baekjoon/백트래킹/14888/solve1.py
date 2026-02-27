import sys
def input():
  return sys.stdin.readline().rstrip()

N = int(input())
numbers = list(map(int,input().split()))
opers = list(map(int,input().split()))
dep = sum(opers)

max_value = -float('inf')
min_value = float('inf')
#각 숫자의 순서는 동일하게 돌면서 연산자의 순서만 바꿔서 돈다.
#해당 연산자를 돌면서 선택 or 선택하지 않은 경우의 수로 간다.
def dfs(depth,value,op):
   global min_value
   global max_value

   if depth==dep:
    min_value = min(min_value,value)
    max_value = max(max_value,value)
    return
   
   for i in range(4):
     if op[i]>0:
       op[i]-=1

       if i==0:
         dfs(depth+1,value+numbers[depth+1],op)
       elif i == 1:
            dfs(depth+1, value - numbers[depth+1], op)
       elif i == 2:
            dfs(depth+1, value * numbers[depth+1], op)
       else:
            if value < 0:
              dfs(depth+1, -(-value // numbers[depth+1]), op)
            else:
              dfs(depth+1, value // numbers[depth+1], op)
       op[i]+=1

dfs(0,numbers[0],opers)

print(max_value)
print(min_value)
