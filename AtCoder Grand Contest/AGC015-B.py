# AGC015 - B

# floor[i] == "U"のとき) 上階には1回, 下階には2回で行ける
# floor[i] == "D"のとき) 上階には2回, 下階には1回で行ける
# 1階は常に"U",最上階は常に"D"であると制約に定められているので、境界値もなくいたって円滑に実装が可能

from collections import Counter

floor = input()
ans = 0

for i in range(len(floor)):
    #print(i,floor[i])
    if floor[i] == "U":
        ans += (i*2)              # 下の各階に行くのに必要なボタン押下回数を加える
        ans += (len(floor)-i-1)   # 上の各階に行くのに必要なボタン押下回数を加える
    
    if floor[i] == "D":
        ans += (len(floor)-i-1)*2 # 上の各階に行くのに必要なボタン押下回数を加える
        ans += i                  # 下の各階に行くのに必要なボタン押下回数を加える
    #print(":",ans)

print(ans)
