"""
11478. 실버3. sol
"""
s = input()
lst = []

for i in range(len(s)):
  for j in range(len(s)-1,-1,-1):
    #print(i, j, s[i:j+1])
    lst.append(s[i:j+1])
print(len(set(lst))-1)
