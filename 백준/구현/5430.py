from collections import deque

def sol(tmp):
  s = ''
  stack = []
  for i in tmp:
    if i.isdigit():  #숫자라면
      s += i
    else:  #숫자가 아니면
      if s != '':
        stack.append(int(s))  #지금까지의 s를 넣어줌
        s = ''  #다시 초기화
  return stack


n = int(input())

for _ in range(n):
  flag = False #리버스 플래그
  p = input()
  l = input()
  tmp = input()
  q = deque(sol(tmp))
  for i in p:
    if i == 'R':
      if not flag:
        flag = True
      else :
        flag = False
    else:  ##D라면
      if q:
        if not flag :
          q.popleft()
        else :
          q.pop()
      else:
        print('error')
        break
  else:    
    if not flag:
      print("[" + ",".join(map(str, q)) + "]")
    else:
      q.reverse()
      print("[" + ",".join(map(str, q)) + "]")
  
