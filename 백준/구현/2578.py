"""
실버5/ 구현 / sol
"""

from itertools import chain

def row_b(binggo, ans):
    for i in range(5):
        cnt = 0
        for j in range(5):
            if binggo[i][j] == 0:
                cnt += 1
            if cnt == 5: # 한 행 0
                # print("빙고 ROW")
                # print(*binggo, sep='\n')                
                ans += 1
                cnt = 0
    return ans #빙고 x

def col_b(binggo, ans):
    for i in range(5):
        cnt = 0
        for j in range(5):
            if binggo[j][i] == 0:
                cnt += 1
            if cnt == 5: # 한 행 0
                # print("빙고 cOL", ans)
                # print(*binggo, sep='\n')
                ans += 1
                cnt = 0
    return ans #빙고 x 

def rc_b(binggo, ans):
    cnt = 0
    for i in range(5):
        if binggo[i][i] == 0:
            cnt += 1
        if cnt == 5: # 한 행 0
            # print("빙고")
            # print(*binggo, sep='\n')
           return ans+1 #빙고 추가
    return ans 
def cr_b(binggo, ans):
    cnt = 0
    for i in range(5):
        if binggo[i][4-i] == 0:
            cnt += 1
    if cnt == 5: # 한 행 0
        return ans+1 #빙고 추가
    return ans #빙고 x
    
OAOAOAdef check():
    ans = 0
    ans = rc_b(binggo, ans)
OAOAOA    ans = row_b(binggo, ans)
OAOAOA    ans = col_b(binggo, ans)
    ans = cr_b(binggo, ans)   
OAOAOA    return ans         
binggo,ans_lst = [], []
for i in range(5):
    binggo.append(list(map(int,input().split())))


for i in range(5):
    ans_lst.append(list(map(int,input().split())))
ans_lst = list(chain(*ans_lst))
ans = 0
for a in range(25):
    for i in range(5):
        for j in range(5):
            if ans_lst[a] == binggo[i][j]:
                binggo[i][j] = 0
    ans = check()
    # print(f"{a+1}번째, {ans_lst[a]}, {ans}")
    # print(*binggo, sep='\n')
    if ans >= 3:
        print(a+1)
        break


