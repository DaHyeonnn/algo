"""
20115. 실버3. 그리디    
"""
n = int(input())
drink = list(map(int, input().split()))

drink.sort()
# 2 3 6 9 10
ans = drink[-1]
for i in range(len(drink)-1):
    ans += drink[i]/2
    
print(ans)
