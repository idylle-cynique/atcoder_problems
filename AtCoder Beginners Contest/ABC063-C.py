# ABC063 - C
# 提出予定

n = int(input())
tens = []
nottens = []
total = 0

for i in range(n):
      temp = int(input())
      total += temp     # 満点時の得点数を調べておく
      
      if temp%10 == 0:  # 10を約数に持つ得点の問題を格納
            tens.append(temp)
      else:             # 10を約数に持たない得点の問題を格納
            nottens.append(temp)

nottens = sorted(nottens)
                        # 扱いやすいようにソートしておく
#print("tens   :",tens); print("nottens:",nottens)
if total%10 != 0:       # 満点が10の倍数でないならそのまま満点を出力
      print(total)
      exit()
      
if len(nottens) == 0:   # 10を約数に持たない得点の問題が存在しないときは、どうやっても0点にしかならない
      print(0)
      exit()

for i in nottens:       # 小さいものから順に差し引いて、10の倍数でなくなった時点で出力
      total -= i
      if total%10 != 0:
            print(total)
            exit()