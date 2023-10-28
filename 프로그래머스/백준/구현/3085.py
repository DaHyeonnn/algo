"""
백준 실버2 3085 사탕게임
"""
n = int(input())
maps = []
for i in range(n):
  maps.append(list(input()))

def total(maps):
  cnt_lst = []
  for i in range(n):
    cnt = 0
    s = ''
    s = maps[i][0]
    for j in range(n):
      if s == maps[i][j]:
        cnt += 1
      else : 
        s = maps[i][j]
        cnt = 1
      cnt_lst.append(cnt)
  for j in range(n):
    cnt = 0
    s = ''
    s = maps[0][j]
    for i in range(n):
      if s == maps[i][j]:
        cnt += 1
      else : 
        s = maps[i][j]
        cnt = 1
      cnt_lst.append(cnt)
  return max(cnt_lst)
  
dx = [0,1]
dy = [1,0] #우하
cnt_lst = []
for x in range(n):
  for y in range(n):
    for o in range(2):
      nx = x + dx[o]
      ny = y + dy[o]
      if 0<=nx<n and 0<=ny<n:
        a,b = maps[x][y], maps[nx][ny]
        maps[x][y], maps[nx][ny] = b,a
        cnt_lst.append(total(maps))
        maps[x][y], maps[nx][ny] = a,b  #다시 원상태

print(max(cnt_lst))
"""
6
CCPCCC
ADHYKE
DADADA
GHRHRH
DADADA
EHMKUF

"""
        