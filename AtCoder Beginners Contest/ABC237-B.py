# ABC237 - B

'''
    自分で行列計算における転置行列の導出アルゴリズムを実装する問題
    二次元リストを一行目から順に読み込むのではなく、一列目から順に読んでいったものを一行として
    別のリストに格納していけば、それが転置行列になる

    ただし、pythonの場合numpyという行列計算を行える外部ライブラリがあり、
    AtCoderでも利用が可能なため、そちらを利用してもよい
    処理速度はnumpyを利用した場合の方がより高速である
'''
H,W = map(int,input().split())

A = [[int(x) for x in input().split()] for y in range(H)]
B = []

for i in range(W):
    B.append([])
    for j in range(H):
        B[-1].append(str(A[j][i]))

for row in B:
    print(" ".join(row))