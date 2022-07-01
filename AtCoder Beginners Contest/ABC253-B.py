''' ABC253 - B
    文字列でマップが与えられているのでグリッドマップ上の探索アルゴリズム問題
    のようにも見えるが、結局問題で求めているものはなんなのか、を考えてみると
    「oで示された2点間のチェビシェフ距離を求めよ」ということでしかない
    したがって文字列によるマップ情報を読み取った後、二点間の座標を数値に変換し
    チェビシェフ距離を計算して出力するだけでよい

    なおマップそのものはそれほど大きくないので、実際にBFSを用いて解いても
    計算量は大幅に悪化するが問題なく正答判定が得られると思われる
'''

H,W = map(int,input().split())
Field = [list(input()) for _ in range(H)]
start = []
goal = []

for i in range(H):
    #print(Field[i])
    for j in range(W):
        if Field[i][j] == "o":
            if not(start):
                start = [i,j]
            else:
                goal = [i,j]

x = abs(goal[0] - start[0])
y = abs(goal[1] - start[1])
answer = x + y

print(answer)