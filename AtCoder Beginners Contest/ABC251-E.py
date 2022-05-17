''' ABC251 - E
i = 0とi = N-1が相互に接続された関係になっている、という部分的な例外はあるものの、
基本的には入力として与えられた制約をもとに
「i-1番目までの最適を利用してi番目の最適を求める」という処理を繰り返して
全体における最適を求める手法、すなわち動的計画法のアルゴリズムが有効な問題
であると判断できる。

このDPでの基本的な処理方針は
    1) i番目で餌をあげる(1)ときの最適は
        i)  dp[i-1][0] (i-1番目で餌をあげない時+i番目の餌代)
        ii) dp[i-1][1] (i-1番目で餌をあげる時+i番目の餌代)
       のうち最小のもの
    2) i番目で餌をあげない(0)ときの最適は
        i) dp[i-1][1] (i-1番目で餌をあげる時)
       (i-1番目かi番目で餌をあげなければ、すべての動物に餌をあげることができない)
となる

例外部分であるi=0, i=N-1については、そのまま単純に
    1) 1番目(i=0)で餌をあげたときのdp
    2) N番目(i=N-1)で餌をあげたときのdp
の2つを用意し、最後に1)における2)における最適とを比較しより最適なものを解とすればよい
'''

N = int(input())
Fees = [int(x) for x in input().split()]

def print_dp(dp):   # dpテーブルの閲覧
    for row in dp: print(row)
    
dp1 = [[int(0) for x in range(2)] for y in range(N)]
dp2 = [[int(0) for x in range(2)] for y in range(N)]

for i in range(1,N): # 1番目で餌をあげない場合でdp
    for j in range(2):
        if i == 1:     # 1番目(i=0)で餌をあげない場合、2番目(i=1)では必ず餌をあげる必要がある
            dp1[i][j] = dp1[i-1][j] + Fees[i]
        elif i == N-1: # N番目でも必ず餌をあげる必要がある
            dp1[i][j] = dp1[i-1][j] + Fees[i]
        else:
            if j: # 餌をあげる時
                dp1[i][j] = min(dp1[i-1][0]+Fees[i], dp1[i-1][1]+Fees[i])
            else: # 餌をあげない時
                dp1[i][j] = dp1[i-1][1]
        
dp2[0][1] = dp2[0][0] = Fees[0]

for i in range(1,N): # 1番目で餌をあげる場合でdp
    for j in range(2):
        if j: # 餌をあげる時
            dp2[i][j] = min(dp2[i-1][0]+Fees[i], dp2[i-1][1]+Fees[i])
        else: # 餌をあげない時
            dp2[i][j] = dp2[i-1][1]


#print_dp(dp1); print(); print_dp(dp2)
answer = min(dp1[-1] + dp2[-1])
print(answer)