"""
실버5 7785 회사에 있는 사람
시작 : 11:22
sol : 11:34
"""

n = int(input())
dic = {}

for i in range(n):
  name, status = input().split()
  if status == "enter":
    dic[name] = 1
  else:
    dic[name] = 0

lst = [key for key,val in dic.items() if val == 1]
lst.sort(reverse=True)
print(*lst, sep='\n')
