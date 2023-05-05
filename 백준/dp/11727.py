"""
실버3:11727 2*n 타일링2
시작: 10:11
sol: 10:27
"""
n = int(input())
dp = [0]*(n+1)
if n<2:
  print(n)
else:  
  dp[1],dp[2] = 1,3
  for i in range(3,n+1):
    dp[i] = (dp[i-2]*2+dp[i-1])%10007
  
  print(dp[n])
