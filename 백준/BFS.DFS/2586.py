"""
실버 1 : 2468 안전영역

문제이해 :
비가 내렸을 때 물에 잠기지 않는 지역이 최대 몇 개 만들어지는가 ?

잠기지 않는 지역 기준 :
잠기지 않는 지역이 상하좌우로 인접해 있음

==> 시작 : 5시 16분
==> 문제 이해 완료 : 5시 25분
==> success : 6시 8분

총평 :
자꾸 80퍼에서 틀려가지고 원인 찾느라 시간을 보냈다 (mincnt는 1임 0이 아니다..)
글고 코드가 조금 비효율적인듯..
"""

from collections import deque

n = int(input()) #크기
lst = []
ma,mi = 1,10 #최댓값을 위한 변수
cnt_lst = []
for i in range(n):
  lst.append(list(map(int, input().split())))
  ma,mi = max(max(lst[i]), ma), min(min(lst[i]), mi) #입력과 동시에 최소/최댓값을 정해주자

def bfs(x,y,rain, lst, visited):
  dx = [0,0,-1,1]
  dy = [-1,1,0,0]
  n = len(lst)
  q = deque()
  q.append((x,y))
  while q:
    x,y = q.popleft() 
    visited[x][y] = 1 #방문처리
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<=nx<n and 0<=ny<n and not visited[nx][ny]: #방문 안했으며
        if lst[nx][ny] > rain : #안잠긴다면
          q.append((nx,ny))
          visited[nx][ny] = 1 #방문처리  
  return visited

for rain in range(mi, ma+1): 
  visited = [[0]*n for _ in range(n)] 
  cnt = 0    #rain이 달라질때마다 초기화
  for i in range(n):
    for j in range(n):
      if not visited[i][j] and lst[i][j] > rain: #방문 안했으면
        bfs(i,j,rain, lst, visited)
        visited[i][j] = 1
        cnt += 1
  cnt_lst.append(cnt)

if max(cnt_lst) == 0: 
  print(1)
else: print(max(cnt_lst)) 


"""
5
6 8 2 6 2
3 2 3 4 6
6 7 3 3 2
7 2 5 3 6
8 9 5 2 7

"""