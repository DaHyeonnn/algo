"""
H-Index. 프로그래머스 sol. 구현
"""
def solution(citations):
    answer = 0
    n = len(citations)
    #citations.sort()
    while 1:
        tmp = sum(1 for item in citations if item>answer)
        if  tmp > answer:
            answer += 1
        else:
            break
        
    return answer


print(solution([3, 0, 6, 1, 5]))
