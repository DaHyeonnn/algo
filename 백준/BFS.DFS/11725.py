"""
백준 실버2 11725 트리의 부모 찾기
시작 : 7:00
종료 : 7:28

bfs로 풀었다 근데 왜 메모리 50184 시간 4360이지..
"""
from collections import deque
n  = int(input())
lst = [[] for _ in range(n+1)]
res = [0]*(n+1)
visited = [False]*(n+1) #방문 기록
for i in range(n-1):
  a, b = map(int, input().split())
  lst[a].append(b)
  lst[b].append(a)

q = deque()
start = 1 #부모루트가 1이므로
q.append(start)
visited[start] = True 
while q:
  start = q.popleft()
  for i in lst[start]:
    if not visited[i]:
      res[i] = start
      q.append(i)
      visited[i] = True

for i in range(2,n+1):
  print(res[i])
