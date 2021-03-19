# ABC116-C
n = int(input())
h = [int(x) for x in input().split()]

f = False # 連続する区間を選択中か否かを判定
cnt = 0

max_h = max(h) # 最大値を記録

for high in range(1,100+1):
    #print(high,":",cnt)
    
    for i in range(n):
        #print(h[i],end=" ")
        
        if h[i] >= high:
            f = True
        elif h[i] < high and f == True:
            cnt += 1
            f = False
    
    if f == True:
        cnt += 1
        f = False
        
    #print()
        
    if high > max_h: # h[]の最大値以上を超える高さについてはループ処理の必要がないので終了してよい
        break

print(cnt)
