"""
실버4. 17219. 10/17. sol O
"""
n,m = map(int,input().split())
dic = {}
for i in range(n):
    site, password = input().split()
    if site not in dic:
      dic[site] = password

for i in range(m):
  site = input()
  print(dic[site])

