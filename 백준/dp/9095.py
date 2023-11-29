"""9095. 실3. 123더하기. sol"""
t = int(input())
for i in range(t):
    n = int(input())
    dp = [0]*(n+1)
    for i in range(1, n+1):
        if i<3:
            dp[i] = i
            continue
        if i==3:
            dp[i] = 4
            continue
        dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
    print(dp[-1])
