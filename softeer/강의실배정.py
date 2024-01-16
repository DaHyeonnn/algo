import sys
input = sys.stdin.readline
n = int(input())
stack = []
for i in range(n):
    st,end = map(int, input().split())
    stack.append([st,end])

stack.sort(key = lambda x: (x[1], x[0]))
cnt = 1
tmp = stack[0][1]
for i in range(1,n):
    if tmp <= stack[i][0]:
        cnt += 1
        tmp = stack[i][1]
    
    
print( cnt)
