"""
문제 : 골드5 평범한 배낭

메모리 : 229220 시간 4648 이거 맞나,,
"""
n,m = map(int, input().split()) # 물품 수/ 용량
dp = [[0]*(m+1) for _ in range(n+1)]

for i in range(1,n+1):
  k,v = map(int,input().split())
  for j in range(1,m+1):
    if j-k>=0: #넘치지 않으면
      dp[i][j] = max(dp[i-1][j], dp[i-1][j-k]+v)
    else:
      dp[i][j] = dp[i-1][j]

print(dp[n][m])