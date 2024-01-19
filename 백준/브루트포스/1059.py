import sys
from itertools import combinations
input = sys.stdin.readline

"""
4
1 7 14 10
2
"""
l = int(input())
lst = list(map(int, input().split()))
n = int(input())
lst.sort()
cnt = 0
flag = 0
if n in lst: # n이 리스트에 있다면 그냥 0
  print(0)
else:
  for i in range(1,l):
    if lst[i-1]<=n<=lst[i]:
      flag = 1
      st = lst[i-1]+1
      end = lst[i]-1
      print(st,end)
      break
  if not flag: #포함이 안된다면
    print("flag 0")
    st = 1
    end = lst[0]-1
  tmp = list(map(list,combinations(range(st,end+1),2)))
  for x,y in tmp:
    if x<=n<=y:
      cnt += 1
  
  print(cnt)

