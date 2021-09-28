# ABC220 - C

# ここでは累積和と線形探索を併用したことで線形探索分の計算量がボトルネックとなり処理の遅いチグハグな解答になってしまったが、
# 線形探索分は累積和リストから二分探索で余り分以上の値を求め、そのインデックスを取得することで O(logN) で処理することが可能なはず
# これにより最大計算量もO(logN)で収まり、より高速に動作する
# 追々この実装も実現しておきたい

import itertools

N = int(input())
A = [int(x) for x in input().split()]
X = int(input())

A_acm = list(itertools.accumulate(A))
total = A_acm[-1]

ans_1 = X//total * len(A)
ans_2 = 0

rest = X - ((X//total) * total)

for i in range(len(A_acm)):
        if rest < A_acm[i]:
            ans_2 = i+1
            break
        else:
            pass

print(ans_1 + ans_2)