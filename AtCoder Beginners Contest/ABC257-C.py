''' ABC256 - C
    公式解説とは異なる解法を用いているので、より一般的な解法を取りたい場合には以下を参照
    https://atcoder.jp/contests/abc257/editorial/4181

    問題における解は大体どのくらいの分岐設定値を与えるべきなのか、ということを考えてみると、
        i)  子供の体重の中で大人の体重に近い値
        ii) 体重情報として与えられている値要素群の中の値
    だと推察できる

    であれば、設定値Xをそのまま全列挙で与えるような方法を取らなくとも
    最大でもN(2*10^5)しかない体重情報として与えられた数列の各要素だけ用いて検証を行っても
    f(X)として取ることのできる最大の値を求めることができる、ということになる

    後は、数列(W, Weights)中の要素を用いてXを設定したあと、f(X)の値を求める処理だが、
    これについても愚直な実装では関数fの計算量がO(N)となってしまうので処理が間に合わない
    何かしらの工夫を施して最悪でもO(logN)程度で納めたい
    ここでは子供(S_i,Attributes[i]の設定値が0)と大人(S_i,Attributes[i]の設定値が1)とで
    個別にまとめ昇順にソートしたリストを用意し、関数fに与えたXが各リスト中のどの位置に
    来るのかを二分探索を用いて求め、その位置情報(インデックス)をもとに
        i)  子供を子供として正しく判別できる数
        ii) 大人を大人として正しく判別できる数
    を計算し、この二つの和を求めることで、f(X)の値をO(logN)で求めている

    以上によって全体の計算量はO(N・logN)で収まり、制限時間内に正しい値を求めることができた
'''

import bisect

N = int(input())
Attributes = list(input())
Weights = [int(x) for x in input().split()]

adults = list()
children = list()
WeightsData = dict()

for i,a in enumerate(Attributes):
    if int(a):
        adults.append(Weights[i])
    else:
        children.append(Weights[i])

adults = sorted(adults)
children = sorted(children)
answer = 0

for i,w in enumerate(Weights):
    if int(Attributes[i]):
        w -= 1
    
    adult_pos = bisect.bisect(adults,w)
    child_pos = bisect.bisect(children,w)
    #print(w,child_pos,len(adults) - adult_pos)
    score = child_pos + len(adults) - adult_pos
    answer = max(answer,score)

print(answer)