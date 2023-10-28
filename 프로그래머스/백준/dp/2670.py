"""
백준 실버4 2670 sol
"""
n = int(input())
lst = []
for i in range(n):
  lst.append(float(input()))
dp = [0]*n
ans,dp[0] = lst[0],lst[0]

for i in range(1,n):
  if lst[i]*ans > lst[i]:
    ans = lst[i]*ans
  else:
    ans = lst[i]
  dp[i] = ans
print(f'{max(dp):.3f}')
  