"""
1822. 실버4. 차집합. sol
"""
n,m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(set(a)-set(b))
c.sort()
print(len(c))
print(*c, sep=" ")
