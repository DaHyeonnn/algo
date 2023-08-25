def solution(x, y, n):
    answer = 0
    memorize = [1e9] * (y+1)
    memorize[x] = 0
    for i in range (x, y+1):
        if i + n <= y:
            memorize[i+n] = min(memorize[i+n], memorize[i] + 1)
        if i * 2 <= y:
            memorize[i*2] = min(memorize[i*2], memorize[i] + 1)
        if i * 3 <= y:
            memorize[i*3] = min(memorize[i*3], memorize[i] + 1)
    
    if memorize[y] == 1e9:
        return -1
    return memorize[y]

    """
    #### 1차 풀이 => 75점 ####
def solution(x, y, n):
    answer = 0
    dp = [1000001]*(y+1)
    dp[x] = 0

    for i in range(x+1,y+1):
        if i % (x*6) == 0:
            dp[i] = min(dp[i//2], dp[i//3])+1
        elif i % (x*2) == 0:
            dp[i] = dp[i//2]+1       
        elif i % (x*3) == 0:
            dp[i] = dp[i//3]+1
        if i-n >= 0:
            dp[i] = min(dp[i], dp[i-n]+1)
   
    return dp[y] if dp[y] != 1000001 else -1
    """