import sys

n,k = map(int, input().split())
s = list(input().rstrip())
dp = [0]*n

for i in range(n):
    if s[i] == "P": #로봇이라면
        l,r = i-k, i+k #각각의 왼쪽 오른쪽 인덱스
        for j in range(l,r+1): #왼쪽부터 오른쪽 모두 탐색
            if j==i:
                continue
            if 0<=j<n: #범위내에 존재하고
                if s[j] == "H"and not dp[i]: #그 위치에 부품이 존재하고 해당 로봇위치가 아직 1로 안됐다면
                    dp[i] = 1
                    s[j] = 'a'
                    break
#print(dp)
print(dp.count(1))

