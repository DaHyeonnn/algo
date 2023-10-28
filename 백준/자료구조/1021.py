"""
실버 3 : 1021 회전하는 큐
시작 : 4:01
success : 4:53

총평 : 생각보단 어렵진 않았다.
예제4에서 자꾸 답이 안 나와서 확인해보니 
조건문에서 ceil해줘야한다..다 print문 찍어봤다.......
연산 2가 연산 3보다 1씩 적게 나오기 때문에, 
최대한 연산 2로 계산해야함
"""
from collections import deque
import math
n,m = map(int,input().split()) #전체 크기와 뽑을 수 크기
lst = list(map(int, input().split())) #뽑고 싶은 수와 순서
cnt = 0 #연산 횟수
# 1 2 3 : 즉 1 2 3 순서대로 뽑고 싶음

#일단 1~n까지 숫자 리스트 만들어주자
q = [i+1 for i in range(n)] #1~n
q = deque(q)


#왼쪽으로 도는게 빠를지 오른쪽으로 도는게 빠를지 정해야함
for i in range(m):
  while 1: 
    if q[0] == lst[i] : # 1번 연산
      q.popleft()
      break
    if q.index(lst[i])+1 <= math.ceil(len(q)/2) : #2번 연산이 더 유리한 경우 (앞을 삭제)
      tmp = q.index(lst[i])
      for _ in range(tmp):
        q.append(q.popleft())
      cnt += tmp
    else:  #그 외는 그냥 필요없는건 모두 앞으로 꺼내주자..?
      tmp = len(q)-q.index(lst[i])
      for _ in range(tmp):
        q.appendleft(q.pop()) #3번 연산 뒤에부터 삭제 후 맨 앞에 추가
      cnt += tmp
print(cnt)


"""
10 3
2 9 5
"""
    