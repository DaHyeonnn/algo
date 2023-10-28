
import sys
input = sys.stdin.readline
 
n = int(input())
cnt = 0
 
for _ in range(n):
    word = input().rstrip()
    stack = []
    for i in range(len(word)):
        if stack and word[i] == stack[-1]:
            stack.pop()
        else: #스택 비어있거나 다를 경우
            stack.append(word[i])
    if not stack:
        cnt += 1
print(cnt)