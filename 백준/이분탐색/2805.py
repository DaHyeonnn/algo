"""
절단기에 설정할 수 있는 높이의 최댓값을 출력해야 함.
"""
n,m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
ans,st,end = 0,1,lst[n-1]

def tree(lst,mid):
  res = 0
  for i in range(n):
    tmp = lst[i]-mid
    if tmp > 0:
      res += tmp
  return res
  
while st<=end:
  mid = (st+end)//2
  tmp = tree(lst,mid)
  if m <= tmp:
    ans = mid
    st = mid + 1
  else:
    end = mid -1

print(ans)