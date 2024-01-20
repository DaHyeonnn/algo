import sys
input = sys.stdin.readline
from itertools import permutations
from collections import deque
n,m,k = map(int, input().split()) #레일 개수, 바구니 무게, 일 횟수
rail = list(map(int, input().split()))
answer = sys.maxsize
lst = permutations(rail, n)

        
for stack in lst:
    stack = list(stack)
    tmp = 0
    cnt = 0
    res = 0 #전체 합
    idx = 0 #인덱스
    while cnt != k:
        if tmp + stack[idx] <= m:
            tmp += stack[idx]
            stack.append(stack[idx])
            idx += 1
        else : #초과한다면
            res += tmp
            tmp = 0
            cnt += 1
    answer = min(res, answer)
print(answer)
