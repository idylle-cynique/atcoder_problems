# Educational DP Contest - D

'''
 二次元のDPテーブルを用いて行う動的計画法プログラム
 価値として与えられる値の範囲が最大10^9と大きい一方、重さとして与えられる値が10^5と小さいことを利用して
 DPテーブルを生成し次のように定義すればよい
 「dp[i][j] Goodsのi番目まで使ってj以下の最大の重さまでナップサックに詰め込んだ場合の価値の最大値」
 この場合の計算量はO(N・Capacity)で、DPテーブルのためのループ処理は最大でも10^2 * 10^5 = 10^7程度となり
 十分高速に解を求めることができる
'''

N,Capacity = map(int,input().split())
Goods = sorted([[int(x) for x in input().split()] for y in range(N)])
dp = [[0]*(Capacity+1) for _ in range(N+1)]

def view_dp(DP):
    for r in DP:
        print(r)
    print()
    return True

for j in range(1,Capacity+1):
    for i in range(1,N+1):
        #print("品物の{:}番目まで使って{:}以下の最大の重さまでナップサックに詰め込んだ場合の価値の最大値を考える".format(i,j))
        GoodsWeight,GoodsValue = Goods[i-1]
        
        if GoodsWeight <= j:     # i番目の荷物をナップサックに入れる(入れられる)場合
            # (1) i-1番目までの荷物を使って重さjまで荷物を詰め込んだときの価値の最大値
            # (2) i番目の荷物を入れたときの価値の増加分 + j-(i番目の荷物分の重さ)までの重さになるまで荷物を詰めたときの価値の最大値
            # のうち、より価値の総和が大きくなるものがこの場合の解にあたる
            dp[i][j] = max(dp[i-1][j], GoodsValue + dp[i-1][j-GoodsWeight])
        else:                    # i番目の荷物をナップサックに入れない(入らない)場合
            # i-1番目までの荷物を使って重さjまで荷物を詰めたときの価値の最大値が、この場合の解にあたる
            dp[i][j] = dp[i-1][j] 
        
        #view_dp(dp)

print(dp[-1][-1])