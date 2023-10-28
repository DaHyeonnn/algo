def solution(land):
    for i in range(1,len(land)):
        for j in range(len(land[0])): 
            if j == 0: 
                land[i][j] += max(land[i-1][1:])
            elif j == len(land[0])-1:
                land[i][j] += max(land[i-1][:j])
            else :
                land[i][j] += max( max(land[i-1][:j]), max(land[i-1][j+1:]) )
    return max(land[-1])

"""
프로그래머스 dp 문제
"""