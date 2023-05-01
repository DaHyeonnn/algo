"""
백준 실버3 9375 패션왕 신해빈

"""
t = int(input())
for _ in range(t):
  n = int(input()) #옷 수
  dic = {}
  for _ in range(n):
    cloth, name = input().split() #옷과 종류
    if name not in dic: #새로운 종류면
      dic[name] = [cloth]
    else : 
      dic[name].append(cloth)
  res = 1
  cnt = 0
  print(dic)
  for k,v in dic.items():
    res *= len(v)+1
  # if len(dic.keys()) != 1:
  #   res += cnt
  print(res-1)  