# ABC095 - C
a,b,c,x,y = [int(x) for x in input().split()]
ans = 0

ans += min((a+b)*min(x,y),c*2*min(x,y))
                  # 先ずmin(x,y)個まで買うときのパターンを考える
                  
if x == y:
      print(ans)
      exit()
      
if x > y:         # 足りないピザの情報を記録
      rest = ["x",max(x,y)-min(x,y)]
else:
      rest = ["y",max(x,y)-min(x,y)]


if rest[0] == "x":
      ans += min(a*rest[1],c*2*rest[1])
else:
      ans += min(b*rest[1],c*2*rest[1])

print(ans)