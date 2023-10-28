    """
    실버 3 / 단어 뒤집기 / 풀이참고
    """
s = input() + ' '
stack = []
flag = False # 괄호 안에 있는지 여부
answer = ''

for i in s:
  if i == "<":
    flag = True #괄호 안에 있음
    for _ in range(len(stack)):
      answer += stack.pop()
  stack.append(i)

  if i == ">":
    flag = False
    for _ in range(len(stack)):
      answer += stack.pop(0)

  if i == " " and not flag:
    stack.pop()
    for _ in range(len(stack)):
      answer += stack.pop()
    answer += ' '

print(answer)