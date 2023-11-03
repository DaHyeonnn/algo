from collections import defaultdict
"""
신고결과받기. 나중에 다시 풀어보자. defaultdict의 유용성을 알게 됐당
"""

def solution(id_list, report, k): 
    answer = [0]*len(id_list)
    id_dic = defaultdict(list)
    report = list(set(report))
    stop_id = defaultdict(int)
    for i in range(len(report)):
        sour, des = report[i].split(" ")
        id_dic[des].append(sour) 
    for i in range(len(report)):
        sour, des = report[i].split(" ")
        if len(id_dic[des]) >= k: #신고가 k번 넘으면 => 정지수준이면 des에게 메일을 보내야 함
            answer[id_list.index(sour)] += 1

    
    return answer


