''' ABC213 - B
    配列に格納してスコア順でソートするだけでよい
    ここではキーの指定などをせずにsorted関数をそのまま利用するだけで問題の処理が出来るよう
    [選手番号, スコア] ではなく [スコア, 選手番号] という形で値を格納し、
    昇順ではなく降順でソートしている
'''

N = int(input())
Players = [[int(x)] for x in input().split()]

for i in range(N):
    Players[i].append(i+1)

Players = sorted(Players,reverse=True)
print(Players[1][1])