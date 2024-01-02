n, length = map(int, input().split())
dp = [0 for i in range(10001)]
dp[1] = 1
lst = []
for t in range(n):
    s,e,l = map(int, input().split())
    l = min(e-s, l)
    lst.append([s,e,l])
    
lst = sorted(lst, key=lambda x:x[0])
for t in range(n):
    s,e,l = lst[t]
    for i in range(2, length+1):
        if dp[i] == 0:
            dp[i] = dp[i-1]+1 #아직 측정 안 한 지점이므로 +1
        else:
            dp[i] = min(dp[i-1]+1, dp[i]) #이미 측정됐을 수 있으니 dp[i]와 dp[i-1]+1을 비교
        
        if i == e: #지름길 도착지점         
            dp[i] = min(dp[i], dp[s]+l)
            
        
print(dp[length])
