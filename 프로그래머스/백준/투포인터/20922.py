"""
백준 실버1 20922 겹치는 건 싫어

틀림. 다른 사람 풀이 참고
9 2
3 2 5 5 6 4 4 5 7
"""

n,k = map(int, input().split())
lst = list(map(int, input().split()))
left, right = 0, 0

cnt = [0] * (max(lst)+1)
answer = 0
while right < n: #끝까지 다 돌기
  if cnt[lst[right]] < k :
    cnt[lst[right]] += 1
    right += 1
  else :
    cnt[lst[left]] -= 1
    left += 1
  answer = max(answer , right-left)

print(answer)