# 별 찍기 - 5
N = int(input())
for i in range(1, N + 1) : 
    blank = " " * (N - i)
    star = "*" * (2*i-1)
    print(f"{blank}{star}")