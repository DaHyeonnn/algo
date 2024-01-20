import sys
input = sys.stdin.readline
r,c,k = map(int, input().split())
maps = []
dx,dy = [-1,0,1,0], [0,1,0,-1]
for _ in range(r):
  maps.append(list(input()))
cnt = 0 #길이가 k인 횟수
visited = [[0]*c for i in range(r)]
def dfs(d,x,y):
  visited[x][y] = 1
  global cnt
  if d==k:
    if x==0 and y==c-1: #도착지점이라면
      cnt += 1
    return 
  for i in range(4):
    nx,ny = x+dx[i], y+dy[i]
    if 0<=nx<r and 0<=ny<c and maps[nx][ny] != 'T' and visited[nx][ny] == 0: #방문하지 않았으며 갈 수 있다면
      visited[nx][ny] = 1 #방문처리
      dfs(d+1,nx,ny)
      visited[nx][ny] = 0 #방문처리 해제
      

dfs(1,r-1,0) #거리,x시작좌표,y시작좌표
print(cnt)
