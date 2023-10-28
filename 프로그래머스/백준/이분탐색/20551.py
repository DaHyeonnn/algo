"""
(틀)
백준 20551번 실버4 sort 마스터 배지훈의 후계자
"""

## 1번 풀이
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
lst = []
for _ in range(n):
  lst.append(int(input()))
lst.sort()
dlst = {}

for idx,val in enumerate(lst):
  if val not in dlst:
    dlst[val] = [idx]
  else: 
    dlst[val].append(idx)


for _ in range(m):
  val = int(input())
  if val in dlst:
    print(dlst[val][0]) #가장 첫 번째 인덱스
  else:
    print(-1)
"""
도저히 이진탐색으로 안 풀려서 다른 사람 풀이 참고했는데,,
딕셔너리로 접근하면 되네 나 왜 생각도 못 했냐
"""

## 2번 풀이
from bisect import bisect_left
import sys

N,M = map(int,sys.stdin.readline().split())

A = [ int(sys.stdin.readline()) for _ in range(N) ]

A.sort()

D = [ int(sys.stdin.readline()) for _ in range(M) ]


for i in D:
    ans = bisect_left(A,i)
    if ans >= N:
        print(-1)

    elif A[ans]==i:
        print(ans)
    else:
        print(-1)

"""
와 bisect_left(list, index) : 정렬된 리스트에 i가 들어갈 때 어느 위치에 삽입되어야하는지 인덱스를 반환.......
ㅋㅋㅋㅋㅋㅋㅋ
"""