"""
11048 
시작 : 11:31
sol : 11:52
코드가 이쁘지 않음
"""
n,m = map(int,input().split())
miro = []

for _ in range(n):
  miro.append(list(map(int,input().split())))

for i in range(n):
  for j in range(m):
    if i==0 and i==j:
      continue
    elif i==0:
      miro[i][j] += miro[i][j-1]
      continue
    elif j==0:
      miro[i][j] += miro[i-1][j]
      continue  
    miro[i][j] += max(miro[i-1][j],miro[i][j-1],miro[i-1][j-1])

print(miro[n-1][m-1])