# ARC003 - A

# 問題文の通りに処理を実装すればよい。制約も 1 <= N <= 100と小さいので、特に工夫する必要はない
# ただし、仮にNの制約が10^6を超える大きな値だった場合でも高速に処理できるよう、
# collectionsライブラリを使って各グレードの出現回数を事前に整理してからGPAの算出処理を行うようにした
# この場合for文のループ回数は常に5回で終えられるので、愚直に処理した場合最大で95回ループ処理回数を削減できる

import collections

N = int(input())
Result = list(input())

point_dict = {"A":4, "B":3, "C":2, "D":1, "F":0}
Result_data = collections.Counter(Result)
total_point = 0

for k,v in Result_data.items(): # items()でキーと値の両方を取り出す
    #print(k,":",v)
    total_point += (point_dict[k]*v) # (重みづけ*実得点)を総合得点として加点

print(total_point/N) # 単位数で割って出力
