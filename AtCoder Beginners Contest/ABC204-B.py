# ABC204 - B

# 要求されたとおりに実装を行えばよい問題
# 以下・未満・以上などの語に注意して、境界値での処理を誤らないこと

N = int(input())
A = [int(x) for x in input().split()]
ans = 0

for ele in A: 
    if ele <= 10: # 実っている木の実が10個以下の時
        pass
    else:         # 実っている木の実が10個より多いとき
        ans += (ele-10)

print(ans)