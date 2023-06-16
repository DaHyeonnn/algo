"""
백준  실버5 1251번 단어나누기
"""
s = list(input())
n = len(s)
lst = []
for i in range(1, n-1):
  for j in range(i+1, n):
    tmp1 = s[:i]
    tmp2 = s[i:j]
    tmp3 = s[j:]
    
    result = "".join(tmp1[::-1]) + "".join(tmp2[::-1]) + "".join(tmp3[::-1])
    print(tmp1,tmp2,tmp3, result)
    lst.append(result)

lst.sort()
print(lst[0])