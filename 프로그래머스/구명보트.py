def solution(people, limit):
    answer = 0
    st, end = 0,len(people)-1
    people.sort()
    while st < end:
        tmp = people[st] + people[end]
        if tmp <= limit:
            answer += 1
            st += 1
        end -= 1
      
    return len(people)- 2*answer + answer