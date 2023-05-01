"""
문제 : 실버4 1057 토너먼트
시작/끝 : 4:50 / 5:10

==> 시간초과..
다른 사람 풀이 참고함

솔직히 시간차이가 어디서 나는지..? 싶다
math.ceil를 해줄 필요없이 걍 빼주면 되는군..

==> while을 빠져나오는 조건에서 시간초과 발생한 것
a == b이면 빠져나오자.. 
"""

import sys
import math
input =sys.stdin.readline
n,a,b = map(int,input().split())

cnt = 0
while 1:
  if a == b: #a가 홀수이며 바로 옆에 존재할 때
    break
  cnt += 1
  a = math.ceil(a/2)
  b = math.ceil(b/2)

print(cnt)


"""
테케는 통과했으나 시간초과 코드
import math
import sys
input =sys.stdin.readline
n,a,b = map(int,input().split())

cnt = 1
while 1:
  if a%2==1 and b-a==1: #a가 홀수이며 바로 옆에 존재할 때
    break
  cnt += 1
  a = math.ceil(a/2)
  b = math.ceil(b/2)

print(cnt)


다른 사람 코드
n, kim, im = map(int, input().split())
count = 0
while kim != im:
    kim -= kim // 2
    im -= im // 2
    count += 1
print(count)

"""