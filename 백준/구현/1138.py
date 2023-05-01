"""
방법 1:
index를 val만큼 띄어 값을 넣어주자. 만약 값이 비어있지 않다면, +1씩 해주며 비어있는 곳에 넣어주자
==> 예제입력 4에서 틀림

방법 2:
0의 개수를 세서 그만큼 띄어주자
==> 성공 but 코드 개더럽다 ㅋㅋㅠ
"""
n = int(input())
lst = list(map(int, input().split())) #입력 리스트
ans = [0]*n #정답 리스트
for i in range(n):
  idx = 0
  tmp = lst[i] #0의 개수와 비교하기 위한 변수
  while 1:
    if ans[:idx+1].count(0) >tmp and ans[idx]==0:
      ans[idx] = i+1
      break
    else:
      idx += 1
      
print(*ans, sep=' ')
