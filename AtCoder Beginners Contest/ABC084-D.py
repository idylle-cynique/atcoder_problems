# ABC084 - D

# エラトステネスのふるいのアルゴリズムを用いて高速に素数リストを作成すること
# 累積和を理解して適切に用いることで、クエリからの処理をO(1)で返せるようにすること
# の2点が求められる。

import math

def elatos(n):
      x = 2
      shieve = set([int(x) for x in range(2,n+1)])
      garbage = set()
      check_list = set()

      while(x*x < n):
            garbage = set([x*int(i)+x for i in range(1,n//x+1)])
            shieve -= garbage
            check_list.add(x)
      
            x = min(shieve-check_list)
      
      return shieve

n = 10**5

elatos_shieve = elatos(n) # 事前に10**5までの素数を得ておく
elatos_acum = []
c = 0

for i in range(10**5+1):
      if i in elatos_shieve and (i+1)//2 in elatos_shieve:
            c += 1
            elatos_acum.append(c)
      else:
            elatos_acum.append(c)
      
#print(elatos_shieve); print(elatos_acum)

q = int(input())

for i in range(q):
      l,r = [int(x) for x in input().split()]
      
      #print(elatos_acum[r],elatos_acum[l])
      print(elatos_acum[r]-elatos_acum[l-1]) # l以上r以下なので、添え字l未満(l-1)の数までとする必要がある
      
