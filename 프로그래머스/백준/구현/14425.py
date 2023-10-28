"""
실버3 14425 문자열 집합
시작 : 11:08
sol : 11:14
"""
n, m = map(int, input().split())
ans = 0
s = {}
for i in range(n):
  name = input()
  s[name] = 0

for i in range(m):
  name = input()
  if name in s:
    ans += 1

print(ans)
