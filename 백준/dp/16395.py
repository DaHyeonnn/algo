"""
실버5 16395 파스칼의 삼각형

1
1 1
1 2 1
1 3 3 1
1 4 6 4 1 (5,3 => 4,2)

시작 : 7:20
sol : 7:33
"""

n, k = map(int, input().split())
dp = [[1]*(i+1) for i in range(n) ]

for i in range(2,n):
  for j in range(1,len(dp[i])-1): #양 끝은 제외해줌
    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]


print(dp[n-1][k-1])