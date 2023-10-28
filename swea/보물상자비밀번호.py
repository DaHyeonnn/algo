"""
swea 보물상자 비밀번호
sol
옹 swea 처음 풀어봤다
그냥 자료구조 문제인 듯
"""


def check(lst, k):
  l = len(lst) // 4  #한 변의 길이
  stack = []  #스택
  for _ in range(l):
    for i in range(4):
      if "".join(lst[l * i:l * (i + 1)]) not in stack:  #없으면
        stack.append("".join(lst[l * i:l * (i + 1)]))
    lst.insert(0, lst.pop())  #하나씩 회전

  for i in range(len(stack)):
    stack[i] = int(stack[i], 16)

  stack.sort(reverse=True)
  return stack[k - 1]


n = int(input())
for _ in range(n):
  a, k = map(int, input().split())  #총길이와 k
  lst = list(input())
  print("#1 ", check(lst, k))
"""
5
12 10
1B3B3B81F75E
16 2
F53586D76286B2D8
20 14
88F611AE414A751A767B
24 16
044D3EBA6A647B2567A91D0E
28 11
8E0B7DD258D4122317E3ADBFEA99

"""
