"""
실버 2 : 1058 친구
시작 : 11:00
성공 : 11:34

총평 : 
비효율적..? 삼중for문 사용함 
글고 플로이드 와샬 알고리즘 문제인데, 적용안함
사실 그게 뭔지 모른다 공부하자,,
"""
import copy
n = int(input()) #사람 수
map=[] #친구 맵
for _ in range(n):
  map.append(list(input()))

vmap = copy.deepcopy(map)

for i in range(n):
  cnt = 0 #친구 수
  for j in range(n):
    if i == j : #자기 자신은 제외해주자
      continue
    if vmap[i][j] == 'Y': #친구라면, 이 사람의 친구도 친구일 수 있음
      for idx in range(n):
        if vmap[j][idx] == 'Y': 
          # print(i,j, idx)
          map[i][idx] = "Y" #친구의 친구인 경우니 y로 바꿔주자

cnt = 0
for i in range(n):
  cnt = max(cnt, map[i].count("Y"))

if cnt > 1: print(cnt-1)  
else : print(0)
      