"""
백준 1074 실버1 sol
분할정복 문제인데, 맞긴 했는데 이상하게 푼 듯...
이걸 맞네..
"""

n,r,c = map(int, input().split())
idx = 0


tmp = 0
while 1:
  if n == 0:
    print(tmp)
    break
  tmp_x = r//(2**(n-1))
  tmp_y = c//(2**(n-1))

  tmp += ((2**n)**2//4)*(tmp_x*2 + tmp_y)
  r %= (2**(n-1))
  c %= (2**(n-1))
  n -= 1


""" 아래는 메모리 초과난 코드이다. maps 리스트에 값을 하나씩 걍 다 넣어줬기 때문에 당연한 결과임"""
# maps = [[0]*(2**(n)) for _ in range(2**(n))]

# def sol(maps, i,j, idx):
#   maps[i][j] = idx
#   maps[i][j+1] = idx+1
#   maps[i+1][j] = idx+2
#   maps[i+1][j+1] = idx+3

# for i in range(0,2**n,2):
#   for j in range(0,2**n,2): 
#     sol(maps, i,j, idx)
#     idx += 4

# print(maps[r][c])
