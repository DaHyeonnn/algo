"""
12919. A와 B 2. 골드5. 10/20.
- 문자열 뒤에 A 추가
- 문자열 뒤에 B 추가하고 뒤집기
반대로는
- 뒷문자가 A라면 빼기
- 뒤집은 상태의 뒷 문자가 B라면 뒤집고 빼기

백준 질문게시판을 보니, t에서 하나씩 빼면서 s에 맞춰나가야 시간초과에 걸리지 않는다고 한다. 시간초과 난 코드(s에서 하나씩 추가해서 t를 만드는 경우)는 2의 제곱이 되기 때문에 시간이 초과되는 것 같다.
그래서 반대로 접근해야한다는 힌트를 얻어서 풀게 되었다.
"""
s = input()
t = input()


def sol(l, s, t):
  #print(f"{l}: {s}, {t}")
  if l < len(s) or l == 0:
    return 0

  if s == t:
    print(1)
    exit()
  if t[-1] == 'A':
    sol(l - 1, s, t[:-1])
  if t[0] == "B":
    sol(l - 1, s, str(t[::-1])[:-1])
  return 0


print(sol(len(t), s, t))
"""
### 시간초과
def sol(l, s): #depth, 문자열,
  if l > len(t):
    return 0
  else:
    if str(s) == str(t):
      print(1)
      exit()
  sol(l+1, str(s)+'A')
  sol(l+1, str(s + 'B')[::-1])
  return 0
print(sol(1,s))
"""

