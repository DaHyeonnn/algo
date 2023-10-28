"""
백준 실버1 음식물 피하기 bfs
"""
from collections import deque
n,m,k = map(int,input().split())
maps = [[0]*m for i in range(n)]
dx = [0,0,-1,1]
dy = [-1,1,0,0]
ans = 0

for i in range(k):
  a,b = map(int, input().split())
  maps[a-1][b-1] = 1

def bfs(x,y):
  ans = 0
  maps[x][y] = 0 # 방문처리
  q = deque()
  q.append((x,y))
  while q:
    x,y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<=nx<n and 0<=ny<m:
        if maps[nx][ny] != 0: #방문 안 했다면 (=쓰레기라면)
          maps[nx][ny] = 0
          ans += 1
          q.append((nx,ny))
  return ans+1

for i in range(n):
  for j in range(m):
    if maps[i][j] : #쓰레기인 경우
      ans = max(ans, bfs(i,j))
print(ans)