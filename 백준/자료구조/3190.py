"""
3190. 뱀. 골드4. 10/19. => 어찌어찌 해결
"""
#### 입력
from collections import deque

n = int(input()) #보드 크기
k = int(input()) #사과 개수
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0] #동남서북
maps = [[0]*n for _ in range(n)] #게임 맵
l_sec = {} #방향 변환 시간표
### k개의 사과의 위치
for _ in range(k):
  x,y = map(int, input().split())
  maps[x-1][y-1] = 1 #사과 맵에 입력
l = int(input()) # 방향 변환 수
for _ in range(l):
  x,c = input().split()
  l_sec[int(x)] = c 


#### 함수
def sol(x,y):
  ans = 0 # 시간
  tmp_l = 0 #처음은 오른쪽을 향해 있음
  q = deque()
  q.append((x,y))
  while 1:
    ans += 1
    
    nx,ny = x+dx[tmp_l], y+dy[tmp_l]
    if 0<=nx<n and 0<=ny<n and maps[nx][ny] != -1 : #맵 안에 있거나 벽이 아니라면
      q.append((nx,ny))
      if maps[nx][ny] != 1: #사과가 없다면
        x,y = q.popleft() #뱀 축소. 제일 먼저 추가해준 좌표를 삭제해주는 것 => 뱀의 꼬리가 사라지는 것임
        maps[x][y] = 0
      # elif maps[nx][ny] == 1 : #사과라면
      maps[nx][ny] = -1 # 뱀 이동했다는 뜻
     
    else : 
      break
    if ans in l_sec: #방향을 바꿔야한다면
      if l_sec[ans] == 'L':
        tmp_l = (tmp_l-1)%4 #왼쪽 방향 변경
      elif l_sec[ans] == 'D':
        tmp_l = (tmp_l+1)%4 #오른쪽 방향 변경
    x,y =nx,ny
    # print(*maps, sep="\n")
    # print(q)
    # print("최종", ans,"  x,y:",x,y, maps[x][y],"\n")
    
  return ans
  
print(sol(0,0))


  
