"""
    실버4 1388 바닥장식 sol
    :예외처리하면서 코드가 매우 더러워졌다.
"""

n,m = map(int, input().split())
lst = []
for i in range(n):
  lst.append(input())

ans = 0

for i in range(n): #가로 '-'
  stack = []
  for j in range(m):
    if not stack and lst[i][j] == '-':
      stack.append(lst[i][j])
      ans += 1
      continue
    if lst[i][j] == '|':
      stack = []
      continue
    if stack[-1] != lst[i][j] and stack[-1] =='-':
      stack.pop()
      stack.append(lst[i][j])

for j in range(m): #세로 '|'
  stack = []
  for i in range(n):
    if not stack and lst[i][j] == '|':
      stack.append(lst[i][j])
      ans += 1
      continue
    if lst[i][j] == '-':
      stack = []
      continue
    if stack[-1] != lst[i][j] and stack[-1] == '|':
      stack.pop()
      stack.append(lst[i][j])

  
print(ans)
      