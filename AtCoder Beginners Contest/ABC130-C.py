# ABC130 - C

# 入力値x,yがそれぞれいかなる値であれ、制約を満たすものであれば常に長方形をちょうど二分割することができる
# すなわち、求められている大きくない方の面積の最大値は常に面積を1/2した値となる

# また、この長方形を二分割する線の引き方が複数あるのは、入力値x,yが長方形の各対角線の交差点の位置にあるときだけ
# この点を踏まえて実装すれば、AC判定が得られる。O(1)なので計算量については考慮が要らない
W,H,x,y = map(int,input().split())

ans_1 = (W*H)/2

if (W-x)==(x-0) and (H-y)==(y-0): # x,yは長方形の各対角線の交差点にあるか？
    ans_2 = 1 # True なら 1
else:
    ans_2 = 0 # Falseなら 0
    
print(ans_1,ans_2)