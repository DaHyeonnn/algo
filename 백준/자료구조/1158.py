"""
문제 : 1158 실버4
"""
n,k = map(int,input().split())

lst = [i for i in range(1,n+1)]

ans = []
tmp = 0

while lst:
  tmp += k-1
  if tmp >= len(lst):
    tmp = tmp%len(lst)  
  ans.append(str(lst.pop(tmp)))

print("<", ", ".join(ans[:]), ">",sep="")