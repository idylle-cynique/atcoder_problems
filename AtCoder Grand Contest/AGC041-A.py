# AGC041 - A
n,a,b = [int(x) for x in input().split()]
cnt = 0

if abs(a-b)%2 == 0:     # 台番号の差が偶数なら、それぞれが近づいていけば必然的に対戦が発生する
      cnt = abs(a-b)//2
      
else:                   # 台番号の差が奇数なら、台番号1もしくはNの台まで行って位置調整を行う必要がある
      to_1 = abs(1-min(a,b))
      to_n = abs(n-max(a,b))
      to_edge = min(to_1,to_n)  # 1とNのうち近い方に接近

      a = abs(a-to_edge)
      b = abs(b-to_edge)
      
      #print("to-edge:",a,b)
      cnt += to_edge + 1        # 位置調整用に1回
      
      if a > b:
            a -= 1
      else:
            b -= 1
      
      #print("adjust :",a,b)
      cnt += abs(a-b)//2        # 後は計算するだけ

print(cnt)