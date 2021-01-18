# ABC121 - C

# 安く売っているところから貪欲に買っていけばよい
n,m = [int(x) for x in input().split()]
drugstores = sorted([[int(x) for x in input().split()] for y in range(n)])
money = 0
#print(drugstores)

for store in drugstores:
      if m > store[1]:  # 残りの必要数がその店の在庫量よりも多いとき
            m -= store[1]
            money += (store[0] * store[1])
      else:             # 残りの必要数がその店の在庫量で事足りるとき
            money += (m * store[0])
            break

print(money)