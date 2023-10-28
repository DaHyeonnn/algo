"""
11279. 최대힙. silver2. heap sol
"""
import heapq
import sys

n = int(input)
heap = []
for _ in range(n):
    node = int(input())
    #print(node, heap)
    if node != 0:
        heapq.heappush(heap, -1*node) # 하나 추가
        
    else : #0이면
        if heap: #비어있지 않으면
            print(-1*heap[0])
            heapq.heappop(heap)
        else: 
            print(0)

