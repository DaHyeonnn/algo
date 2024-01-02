"""
15624. 실버5. 피보나치 수 7. sol 
"""
import sys
input = sys.stdin.readline()
n = int(input)

dp = [0]*(n+1)
if n<1:
    print(0)
elif n==1:
    print(1)
    
else:
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = (dp[i-2] + dp[i-1])%1000000007
    print(dp[-1])
