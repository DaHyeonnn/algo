#실버 3 sol
n = int(input())
dic = {}
for i in range(n):
  a, b = input().split('.')
  if b not in dic:
    dic[b] = 1
  else:
    dic[b] += 1

sorted_dic = sorted(dic.items())

for k, v in sorted_dic:
  print(k, v)
