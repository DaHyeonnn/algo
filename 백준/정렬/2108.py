"""
2108 실버2 sol
코드가 더럽고, 파이썬은 시간초과 뜸
pypy3은 성공 하긴 했는데, 파이썬으로 가능한 코드 풀이 찾아보기
"""
from collections import Counter
n = int(input())
lst = []
for _ in range(n):
  lst.append(int(input()))

lst.sort()
dic = Counter(lst)
max_cnt = max(dic.values())
dic_val = list(dic.values())
max_freq = dic_val.count(max_cnt)
max_freq_lst = []
for k,v in dic.items():
  if v == max_cnt :
    max_freq_lst.append(k)

#출력부분
print(int("{:.0f}".format(sum(lst)/n)))
print(lst[n//2])
if max_freq > 1: #여러 개 존재하면
  print(max_freq_lst[1])
elif max_freq == 1: #한 개면
  print(max_freq_lst[-1])

print(lst[-1]-lst[0])
  

"""
5
1
3
8
-2
2
"""