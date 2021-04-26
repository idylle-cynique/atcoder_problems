# ABC131 - D

N = int(input())
tasks = []
total_time = 0 

for i in range(N): # 整列処理がしやすいようにa,bを逆にして二次元リストに格納
    a,b = map(int,input().split())
    tasks.append((b,a)) # bは締切時刻, aは所要時間

tasks = sorted(tasks) # 締切時刻が近い順にソート

for deadline,time in tasks: # 締切時刻が近く、なおかつ所要作業時間が短いものから順に作業していく
    total_time += time
    print(total_time,":",deadline)    
    if total_time > deadline: # 累計作業時間が締切時刻を超過するなら、不可能
        print("No")
        exit()

print("Yes")