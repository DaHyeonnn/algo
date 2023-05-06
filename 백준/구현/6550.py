"""
실버5 6550 부분 문자열
시작 : 10:40
sol : 10:48

"""
from collections import deque
while 1:
  try:
    s,t = input().split()
    s = deque(s)
    for i in range(len(t)):
      if not s: 
        break 
      if s[0] == t[i]:
        s.popleft()
    if s: 
      print("No")
    else :
      print("Yes")
  except:
    break