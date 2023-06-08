"""
10815 실버5 숫자카드
이진탐색에 너무 취약하다. 따로 공부하기!
근데 dict을 사용한게 시간상으로 더 효율적이었음
"""
n = int(input())
sang = list(map(int, input().split()))
m = int(input())
card = list(map(int, input().split()))
ans = []
dic = {}
for i in range(n):
  dic[sang[i]] = 1
  
for i in range(m):
  if card[i] in dic:
    ans.append(1)
  else : ans.append(0)

print(*ans, sep=' ')

"""
1차 시도 : deque => 시간초과
2차 시도 : dict => sol (메모리/시간:113336/716)

+) 다른 풀이 : 이진탐색 (109268/3164)
1. sang을 정렬
2. card에서 card[i]를 하나씩 꺼내면서 low, high, mid 지정
3. sang의 중간 index와 비교
4-1. 중간 값보다 작으면, high를 조절
4-2. 중간보다 크면, low를 조절
4-3. 일치하면 종료 후 1 출력
4-4. 없으면 0 출력

code :
sang.sort()
for i in card:
  low, high = 0, n-1
  flag = False
  while low <= high:
    mid = (low + high)//2
    if sang[mid] > i:
      high = mid - 1
    elif sang[mid] < i:
      low = mid + 1
    else :
      flag = True
      break
  print(1 if flag else 0, end = " ")
      
"""

