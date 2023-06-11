"""
백준 11656 실버4  접미사 배열
"""
s = input()
lst = []
for i in range(0,len(s)):
  lst.append(s[i:])
lst.sort()

print(*lst, sep='\n')