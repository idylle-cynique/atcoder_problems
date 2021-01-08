# ABC175 - C

x,k,d = [int(x) for x in input().split()]
x = -1*x if x < 0 else x # xが負数の場合は正数に直す

if k*d < x: # 0付近まで十分に近づけないときの処理
      ans = x-(k*d)
      print(ans)
      exit()

divxd,modxd = divmod(x,d)     
k_rest = k-divxd  # 正数値の範囲で、0に最も近い位置を求める
x_rest = modxd
if abs(k_rest-d) < k_rest:    # 負距離と正距離のいずれの方がより近いかを考える
      k_rest -= 1
      x_rest -= d

#print(k_rest,x_rest)

if k_rest%2 == 0:             # 残りの移動回数(k_rest)が偶数ならそのままの距離を出力する
      print(abs(x_rest))
else: 
      print(min(abs(x_rest-d),abs(x_rest+d)))