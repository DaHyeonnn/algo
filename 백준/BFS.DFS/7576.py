"""
7576. 토마토. 골드5. 10/18
"""
from collections import deque
m,n = map(int, input().split())
maps = []
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
for i in range(n):
  maps.append(list(map(int, input().split())))
q = deque()

for i in range(n):
  for j in range(m):
    if maps[i][j]==1:
      q.append((i,j))

def bfs():
  while q:
    x,y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<=nx<n and 0<=ny<m :
        if maps[nx][ny] == 0:
          maps[nx][ny] = maps[x][y] + 1
          q.append((nx,ny))


bfs()
res = 0
for i in maps:
  for j in i:
    if j == 0:
      print(-1)
      exit(0)
  res = max(res, max(i))
#print(*maps, sep='\n')
print(res-1)
