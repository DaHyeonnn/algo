"""
백준 실버2 2210 
dfs 공부 다시하기 
"""
def dfs(x,y,num):
  if len(num) == 6:
    if num not in res:
      res.append(num)
    return

  dx = [1,-1,0,0]
  dy = [0,0,1,-1]
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0<= nx < 5 and 0 <= ny < 5:
      dfs(nx,ny, num+maps[nx][ny])

maps = []
res = []
for i in range(5):
  maps.append(list(map(str, input().split())))

for i in range(5):
  for j in range(5):
    dfs(i,j,maps[i][j])

print(len(res))