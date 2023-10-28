"""
실버 4 : 1051 숫자 정사각형
시작 : 11:30
성공 : 11:47

총평 : 시간 초과일 줄 알았는데 성공했따
"""

n,m = map(int, input().split())
s = min(n,m) #정사각형 한 변의 최대 길이
cnt = 1
maps = []
for _ in range(n):
  maps.append(list(map(int,input())))

def sol(maps,x,y,n):
  if maps[x][y] == maps[x+n-1][y] ==maps[x][y+n-1] == maps[x+n-1][y+n-1]:
    return n**2
  else:
    return 1
    
for ss in range(2,s+1): #2,3
  for i in range(n): #0,1,2
    for j in range(m): #0~4
      if 0<=i+ss-1<n and 0<=j+ss-1<m:
        # print(i,j,ss)
        cnt = max(cnt,sol(maps, i, j, ss))

print(cnt)
