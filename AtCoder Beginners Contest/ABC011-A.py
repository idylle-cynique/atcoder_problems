''' ABC011 - A
    そのまま問題での要求通り実装すればよい
    コーナーケース(12)で場合分けを行うやりかたもあるが余り値を利用した方がシンプル
'''

M = int(input())
next_month = M%12 + 1
print(next_month)