"""
1590. 캠프가는 영식. 실버4. 이분탐색인데 다르게 품. 풀이참고함. 나중에 다시
"""

n, t = map(int, input().split())
lst = []
for i in range(n):
    s,i,c = map(int, input().split())
    for idx in range(c):
        tmp = s+i*idx #버스 도착 시간
        lst.append(tmp)
        if lst[-1] > t:
            break
print(lst)
ans = 10000000
for i in lst :
    tmp = i-t
    if tmp >= 0:
        ans = min(ans, tmp)
        
print(ans if ans != 10000000 else -1)        
