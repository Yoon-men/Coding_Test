# 빠른 A + B
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T) : 
    A, B = map(int, input().strip().split())
    print(A + B)