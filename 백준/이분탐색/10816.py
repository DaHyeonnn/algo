"""
실버 4 :
결국, 다른 사람의 풀이를 참고하였음

첫 시도 : 시간 초과 (이분 탐색을 적절히 사용 x)
두 번째 시도 : 역시 시간 초과 / 이분 탐색을 사용했으나, 스택에 너무 많은 값을 append한 것이 문제였을 듯
마지막 시도 : 딕셔너리를 이용
"""
import sys
input = sys.stdin.readline

def bs(lst, tar, start, end):
  #start, end가 들어오면, lst에서 tar를 찾자
  mid = (start+end)//2
  if start > end: # 다 돌았는데, tar이 없는 것
    return 0 
  if tar == lst[mid] : #찾으면
    return lst[start:end+1].count(tar)
  elif tar > lst[mid]:
    return bs(lst, tar, mid+1, end)
  else :  
    return bs(lst, tar, start, mid-1)  
    
n = int(input())
lst = list(map(int, input().split()))
lst.sort()
m = int(input())
target = list(map(int, input().split()))

dic = {}
start,end = [0, len(lst)-1]
for i in lst:
  if i not in dic:
    dic[i] = bs(lst, i, start, end)

print(' '.join(str(dic[x]) if x in dic else '0' for x in target ))