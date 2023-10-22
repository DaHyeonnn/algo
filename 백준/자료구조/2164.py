"""
2164. 카드2. 실버4
제일 위 카드 버리기 => 제일 위 카드 아래로 옮기기
"""
from collections import deque
n = int(input())
lst = [i for i in range(1,n+1)]

q = deque(lst)

while 1:
  if len(q) <= 1:
    break
  tmp1 = q.popleft()
  tmp2 = q.append(q.popleft())

print(q[0])

