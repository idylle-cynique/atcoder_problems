# ABC100 - B

# 解答の数値として考えられる最大の値は 100**3+100**2程度
# 事前に考えられる値のリストをループを用いてまとめておき、すぐに出力できるようにしておく
# n%(100**2) == 0 かつ n%100 == 0のとき、n%(100**3) == 0 かつ n%(100**2)のときなどに注意する必要がある

d_0s = []
d_1s = []
d_2s = []

for i in range(1,100**3+100**2+1):
      if i%(100**3) == 0:
            continue
                  
      if i%(100**2) == 0 and len(d_2s) < 100:
            d_2s.append(i)
            continue
      if i%(100**1) == 0 and len(d_1s) < 100:
            d_1s.append(i)
            continue
      if len(d_0s) < 100:
            d_0s.append(i)
            
#print(d_0s); print(d_1s); print(d_2s)

d,n = [int(x) for x in input().split()]

if d == 0:
      print(d_0s[n-1])
elif d == 1:
      print(d_1s[n-1])
else:
      print(d_2s[n-1])