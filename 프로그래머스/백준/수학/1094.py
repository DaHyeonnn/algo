"""
백준 실버5 1094번
"""
x = int(input())
l,cnt = 64, 0
while 1:
  if l == x:
    print(cnt + 1)
    break
  if l > x: #막대가 더 길다면
    l = l//2 #나누기
    
  else : #막대가 더 짧으면
    x -= l
    cnt += 1
    