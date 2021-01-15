# ABC060 - B
a,b,c = [int(x) for x in input().split()]
mod_set = set()
i = 1

while(True):
      #print(a*i,(a*i)%b,c); print(mod_set)
      if (a*i)%b == c:              
            print("YES")
            exit()
      
      if (a*i)%b in mod_set:  # 既に出た余りがもう一度出てしまった時点で、条件は満足し得ないと判断できる
            print("NO")
            exit()
      
      mod_set.add((a*i)%b)
      i += 1