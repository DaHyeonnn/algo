"""
실버 1 : 1로 만들기 2

<실패 - 풀이 참고함>
연산 횟수의 최솟값은 구했으나 , 그 수를 차례대로 출력하는 과정을 구현하지 못함
dp에 값을 할당해줄 때, 그 인덱스 값을 ans에 넣어주자.
그리고 n부터 0이 될 때까지 탐색해주면 됨

총평 : dp 넘 어렵다 // 나중에 다시 풀어보기 !!!!!!!!!
"""

n = int(input())
dp = [0]*(n+1)
ans = [0]*(n+1)
for i in range(2, n+1):
  dp[i] = dp[i-1]+1
  ans[i] = i-1
  if i%3 == 0 and dp[i] > dp[i // 3] + 1:
    dp[i] = dp[i//3]+1
    ans[i] = i//3
  if i%2 == 0 and dp[i] > dp[i // 2] + 1:
    dp[i] = dp[i//2]+1
    ans[i] = i//2

print(dp[n])
print(n, end=" ")
while ans[n] != 0  :
  print(ans[n], end=" ")
  n = ans[n]



    