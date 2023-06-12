"""
실버4 자료구조 1269 대칭 차집합 sol
"""
a,b = map(int,input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(len(set(A)-set(B)) + len(set(B)-set(A)))