"""
11726. 2*n타일링. 실버3. sol
"""

n = int(input())

dp = [1]*(n+1)
if n == 1:
    print(1)
else :
    dp[2] = 2
    for i in range(3,n+1):
        dp[i] = dp[i-2] +dp[i-1]
    print(dp[-1])
