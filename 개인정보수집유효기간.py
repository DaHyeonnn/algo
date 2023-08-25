def solution(today, terms, privacies):
    answer = []
    dic = {}
    y,m,d = today.split('.')
    today = int(y)*28*12 + int(m)*28 + int(d)
    
    for term in terms:
        p,t = term.split(' ')
        dic[p] = int(t)
    
    for i, privacy in enumerate(privacies):
        collection, term = privacy.split(' ')
        y,m,d = collection.split('.')
        tmp = int(y)*28*12 + int(m)*28 + int(d)
        
        tmp += int(dic[term])*28
        
        if tmp <= today:
            answer.append(i+1)
    return answer