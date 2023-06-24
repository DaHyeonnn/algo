"""
백준 실버2 1182번 부분수열의 합 nosol
: dfs로 하면 되겠다 생각은 했는데 막상 코드를 못 짬

"""

n,s = map(int, input().split())
lst = list(map(int, input().split()))
ans = []
total, cnt = 0,0

def dfs(depth, total):
  global cnt
  if depth == n:
    return
  total += lst[depth]
  if total == s:
    cnt += 1
  
  dfs(depth+1, total)
  dfs(depth+1, total-lst[depth])
  


dfs(0,0)
print(cnt)