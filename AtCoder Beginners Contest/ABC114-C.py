# ABC114 - C
import itertools

n = int(input())
ans = 0

# 3,5,7を用いた３進数のように扱って数を作っていき、その中で条件を満たすものを数え上げていけばよい
# 最大でも3**10程度なので、十分高速に計算が可能

for i in range(3,10):
    picklist = list(itertools.product(["3","5","7"], repeat=i)) # i桁の七五三数の候補リストを作成
    
    for j in picklist:
        if len(set(j)) != 3: # 7,5,3の三個すべて使っていない数は除外
            continue
        
        num = int("".join(j))
        #print(num)
        
        if num <= n:
            ans += 1
        else: # 小さい順に探索を行っているので、それ以上の値が出た時点で処理を終えてよい
            print(ans)
            exit()

print(ans) # コーナーケース(999999999)の時、そのままループが最後まで行くので注意
        