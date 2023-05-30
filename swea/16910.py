"""
SWEA D3 16910 원 안의 점 sol
"""

import math

n = int(input())
x,y,ans = 0,0,0
while 1:
  y = n**2-x**2
  if y<0:
    break
  if x==0:
    ans += int(math.sqrt(y))*2+1
  else : 
    ans += (int(math.sqrt(y)))*4+2
  x+=1


print("#{}".format(test_case),ans)