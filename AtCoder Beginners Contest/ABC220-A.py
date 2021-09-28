# ABC220 - A

# 与えられる数がより大きな数の場合は、今回のような愚直なループ処理は避けること

A,B,C = map(int,input().split())

for n in range(0,1000+1):
    if A <= C*n and C*n <= B:
        print(C*n)
        exit()
        
print(-1)