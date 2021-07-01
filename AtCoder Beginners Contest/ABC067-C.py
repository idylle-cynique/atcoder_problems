# ABC067 - C

# 山の上から何枚か……ということは、
# Snukeが取ったカードの整数の総和はA[0]+A[1]...A[snuke]
# Araiが取ったカードの整数の総和はA[snuke]+A[snuke+1]...A[N-1]
# N枚目を境に山分けした時の1枚目からN枚目までの総和を高速に求める手段があれば
# 0～N枚目まで取って山分けしたときのスコアとして最小のものを探索によって得ることができる

# ここではその実現手段として累積和による事前処理済みのリストを用いた探索を用い
# これによって実現している。このほかにも、尺取り法による計算法でも回答が可能

import itertools

N = int(input())
A = [int(x) for x in input().split()]
Acumulates = list(itertools.accumulate(A)) # A[0]から対応するインデックスまでの要素の総和を並べた累積和リストを生成

sum_A = Acumulates[-1]  # 全ての数列の要素の和を入れておく
ans = 10**9 * (2*10**5) # 解として考えられる値よりも大きな値を入れておく
#print(Acumulates)

for i in range(N-1):
    #print(Acumulates[i],sum_A - Acumulates[i])
    
    # |(0～i-1枚目まで取ったときの総和) - (残りのカードの総和)| のうち、最小をとるものをansに格納
    ans = min(ans,abs(Acumulates[i] - (sum_A - Acumulates[i])))

print(ans)