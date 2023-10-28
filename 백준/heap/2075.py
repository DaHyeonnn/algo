"""
2075. N번째 큰 수. 실버2. 우선순위 큐. 다시
"""
import heapq
n = int(input())
heap = []
for _ in range(n):
    nums = map(int, input().split())
    for num in nums:
        if len(heap) < n:
            heapq.heappush(heap, num) #heap에 n개만큼 넣어 n개 유지
        else : #n개가 차 있다면
            if heap[0] < num: #num이 heap의 최소원소보다 크면
                heapq.heappop(heap) #가장 작은 원소 1개 삭제
                heapq.heappush(heap, num) #num 추가
print(heap[0])
