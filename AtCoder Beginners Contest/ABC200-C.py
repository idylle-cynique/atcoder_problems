# ABC200 - C

# 特定の条件を満たす2つの要素の組み合わせの数を求める数学問題
# O(N^2)による全探索をどうにか工夫して避ける必要がある

# 「差が200の倍数である要素の組み合わせ」という条件について考えていくと
# 200で割ったときの余りが同じである要素の中から2つ選んだとき、がこの条件を満たせる、ということが分かる
# これに従って200で割ったときの余りに応じて一連の要素を辞書型リストを用いて類別すると、O(N)の類別処理後
# 一連の要素を201個の要素からなる辞書型リストに圧縮することが出来る
# あとは辞書型リストから組み合わせが出来るもの(2個以上同じ余りになる要素が存在するもの)について、組み合わせ公式を用いて順番に計算していけばよい

from collections import Counter

N = int(input())
A = [int(x) for x in input().split()]

nums = sorted([A[i]%200 for i in range(N)]) # 受け取った数列を200で割ったときの余りに変換する
tmp_data = Counter(nums) # 各余りを取る要素の数をcollections.Counterで整理しておく
nums_data = {}
#print(nums)
ans = 0

for i in range(200):          # 各余りを取る要素の辞書型リストを初期化
    nums_data[i] = 0

for k,v in tmp_data.items():  # 初期化した辞書に整理したデータを書き込んでいく
    #print(k,v)
    nums_data[k] += v

for k,v in nums_data.items(): # 組み合わせを作ることが出来るものから組み合わせの数を抜き出していく 　
    if v > 0:
        ans += (v*(v-1)) # 計算効率をあげるため、n*(n-1)/(2*1)のうち、"/(2*1)"の部分はここでは計算せずに最後にまとめて行っている

print(ans//2) 