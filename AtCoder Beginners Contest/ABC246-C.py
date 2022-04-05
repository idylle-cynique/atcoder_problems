# ABC246 - C
'''
    クーポンはX円定額値引きするもの(何割割り引くといったものではない)
    なのでどの商品に適用させるかを問題にする必要はない
    
    この部分を踏まえて、ざっくりどのように使えば得をするのか考えてみると
        1) クーポン価額分より値段が大きい商品に、使えるだけ使って値引きしてもらう
        2) それでもクーポンが余った場合は、値引き後残額が大きいものからさらにクーポンを当てて0円にしてもらう
    とすればよいことがわかる。

    後はこれを実際の処理に落とし込むだけでよい    
    ただし、クーポンは最大で10^9枚も与えられるというふうになっているため
    1枚ずつ値引き適用させるような処理ではなく
    MIN(残りのクーポン全部の数, 値引き過ぎにならずに適用可能なクーポンの数)
    を取って、クーポン価額(X円)×使用するクーポンの数で値引きを行うこと
'''

N,K,X = map(int,input().split())
Goods = sorted([int(x) for x in input().split()],reverse=True)
#print(Goods)

coupon_cnt = K
idx = 0

while(coupon_cnt and idx<len(Goods)): # クーポンを使い切るか、全てのクーポンに一通り値引き適用させるまで値引き処理を行う
    cnt = min(coupon_cnt,Goods[idx]//X) # 適用可能なクーポン数よりクーポン所持数の方が下回る場合、ある分だけ使う
    Goods[idx] -= (X * cnt)
    coupon_cnt -= cnt
    idx += 1

# 1円でも多く値引き出来るものから先に値引きできるよう、価格降順に商品を並べ替える
Goods = sorted(Goods, reverse=True)
#print(coupon_cnt,Goods)
idx = 0

# さらに値引きできる場合は、値引きできるだけ値引いていく
while(coupon_cnt and idx<len(Goods)):
    Goods[idx] = max(0,Goods[idx]-X)
    coupon_cnt -= 1
    idx += 1

#print(Goods)
answer = sum(Goods)

print(answer)