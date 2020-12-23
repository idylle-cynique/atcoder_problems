# M-Solutions プロコンオープン2020 - D

n = int(input())
stocks = [int(x) for x in input().split()]
mymoney = 1000
mystock = 0

for i in range(0,len(stocks)-1):     # コメントアウト部分はデバッグ用コード
      #print(stocks[i],stocks[i+1],end=":")
      if stocks[i] < stocks[i+1]:    # 明日の方が株価が高くなる場合は、今日のうちに株を買えるだけ買う
            #print("buying",end=" ")
            mystock += mymoney//stocks[i]
            mymoney = mymoney%stocks[i]
      elif stocks[i] >= stocks[i+1]:  # 明日の方が株価が安くなる場合には、今日のうちに手持ちの株を売却
            #print("selling",end=" ")
            mymoney += mystock*stocks[i]
            mystock = 0
      #print(mymoney,mystock)

i += 1
mymoney += mystock * stocks[i]      # 最終日に手持ちの株をすべて売却して現金化
mystock = 0

print(mymoney)