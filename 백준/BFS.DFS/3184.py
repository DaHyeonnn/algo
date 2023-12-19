"""
[12/19] 3184.양/ silver 1/ bfs/ sol
"""
from collections import deque

r, c = map(int, input().split()) #행,열
lst = []
visited = [[0]*c for _ in range(r)] #방문 확인
dx,dy = [-1,1,0,0],[0,0,-1,1] #상하좌우

for i in range(r):
    lst.append(list(input()))
    

def bfs(x,y):
    v, o = 0,0 #늑대 양 수 초기화
    q =deque()
    q.append((x,y))
    visited[x][y]= 1 #방문처리
    if lst[x][y] == "v":
        v += 1
    elif lst[x][y] == "o":
        o += 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<r and 0<ny<c and lst[nx][ny]!="#" and visited[nx][ny] == 0: #맵 안에 있고 울타리가 아니고 방문안했다면
                if lst[nx][ny] == "v": #늑대라면
                    v += 1 #늑대 카운트 추가
                elif lst[nx][ny] == 'o' :#양이라면
                    o += 1 # 양 추가
                q.append((nx,ny)) #큐에 추가
                visited[nx][ny] = 1 #방문처리
    return o,v

ans_o,ans_v = 0,0 #정답 양과 늑대 수
for i in range(r):
    for j in range(c):
        if lst[i][j] != "#" and visited[i][j] != 1: #울타리가 아니고 방문 안 했으면 bfs 시작
            o,v = bfs(i,j)
            #print(o,v, visited)
            if v >= o : #늑대가 더 많으면 양을 다 먹음
                ans_v += v
            else: #양이 더 많으면 늑대를 쫓아냄
                ans_o += o
print(ans_o,ans_v)
