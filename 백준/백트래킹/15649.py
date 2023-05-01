"""
실버 3. 15649
"""

# 시도 1 : 맞았으나 백트래킹 사용 안 함
from itertools import permutations
n, m = map(int,input().split())
a = [i for i in range(1, n+1)]
lst = list(map(list,permutations(a,m)))

for i in lst:
  print(*i, sep = " ")

