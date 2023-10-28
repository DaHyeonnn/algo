n = int(input())

for _ in range(n):
  s = input()
  stack = [] #스택 초기화
  for i in range(len(s)):
    if not stack: #비어 있으면
      stack.append(s[i])
      continue
    if stack[-1]== "(" and stack[-1] != s[i]:
      stack.pop()
    else:
      stack.append(s[i])
  if stack:
    print("NO")
  else:
    print("YES")