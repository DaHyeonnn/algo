from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(maps, x, y): #지도와 x,y 좌표
    ans = int(maps[x][y]) #현재 방문 위치 값 더해주기
    maps[x][y] = "X" #방문 체크
    q = deque()
    q.append((x,y))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<len(maps) and 0<=ny<len(maps[0]):
                if maps[nx][ny] != 'X': #방문 안 했다면 or 무인도라면
                    q.append((nx,ny))
                    ans += int(maps[nx][ny]) #값 추가
                    maps[nx][ny] = 'X' #방문 처리
    
    return ans
                
                
    
def solution(maps):
    answer = []
    for i in range(len(maps)):
        maps[i] = list(maps[i])
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != 'X': #방문 가능하다면
                answer.append(bfs(maps,i,j))
    if len(answer):
        answer.sort()
        return answer
    else: return [-1]

"""
시작 : 10:05
sol : 10:35

visited 안 쓰려고 하다가 오히려 코드 더 더러워진 것 같다
"""