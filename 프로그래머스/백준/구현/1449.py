"""
실버 3 : 1449 수리공 항승

문제 이해 :
물을 막을 때, 좌우 0.5 간격만큼 줘야함
즉, +1

총평 : 쉬운 문젠데 40분 걸림..
간단한 문젠데 스택만들고, 길이 변수 만들고 난리;;
다 지우고 다시 생각하니 해결했다..
"""

n,m = map(int,input().split()) #개수, 테이프 길이

lst = list(map(int, input().split()))
lst.sort()
cnt = 1
idx = 0
for i in range(1,n):
  if lst[i]-lst[idx]+1 > m: #길이를 넘어가면
    cnt += 1
    idx = i
print(cnt)    
    
