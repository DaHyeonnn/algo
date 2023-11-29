"""
1309. 실버1. 동물원. DP. SOL
"""
n = int(input())
dp = [0]*(n+1)
if n == 1:
    print(3)
elif n == 2:
    print(7)
else :
    dp[1] = 3
    dp[2] = 7
    for i in range(3, n+1):
        dp[i] = (dp[i-2]*3 + (dp[i-1]-dp[i-2])*2) % 9901
    print(dp[-1])

