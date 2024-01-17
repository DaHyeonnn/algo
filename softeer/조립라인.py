import sys

n = int(input())
dp = [[0,0] for i in range(n+1)]
t1,t2 = 0,0
for i in range(1,n):
    a,b,ab,ba = map(int, input().split())

    if i == 1:
        dp[1] = [a,b]
        t1,t2 = ab,ba
        continue
    dp[i][0] = min(dp[i-1][1]+t2, dp[i-1][0]) + a
    dp[i][1] = min(dp[i-1][0]+t1, dp[i-1][1]) + b
    t1,t2 = ab,ba
    #print(dp)

a, b = map(int, input().split())

dp[-1][0] = min(dp[-2][1]+t2, dp[-2][0]) + a
dp[-1][1] = min(dp[-2][0]+t1, dp[-2][1]) + b
#print(dp)
print(min(dp[-1]))
