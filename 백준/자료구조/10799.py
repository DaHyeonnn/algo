"""
실버2 10799 쇠막대기
시작 : 10:50
sol : 11:35
총평 : 맞긴 했지만, 시간도 너무 오래 걸렸고 에러 해결하다보니깐 코드도 넘 더럽고 가독성이 떨어진다.
다른 사람 풀이 보면서 이해하자 !
"""
lst = list(input())
ans,tmp = 0,0 # 막대기 개수
stack = []

i = 0
while i < len(lst)-1:
  if lst[i]=="(" and lst[i+1]==")": #()인 경우
    ans += tmp
    i += 2 # 건너뛰기
    continue
  if not stack or lst[i]=="(":
    stack.append(lst[i])
    ans += 1
    tmp += 1
  elif stack[-1]!=lst[i]: #(~~~)인 경우
    stack.pop()
    tmp -= 1
  i += 1
print(ans)