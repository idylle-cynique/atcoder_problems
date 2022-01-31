# ABC237 - D

'''
    ひとまずサンプルケースを紙に書いて解を求めてみると
    一番最後に入れる値(N)を軸として、後ろから要素を見ていくと
        i)  "L"のコマンドが与えられた値は軸の右側に挿入
        ii) "R"のコマンドが与えられた値は軸の左側に挿入
    という手順をとることで解となる数列が求められることがわかる

    そこまで分かれば、あとはそのまま実装するだけでよい。
    ただし、数列の左端への挿入は通常のリストのままでは挿入処理に
    挿入前のリストの長さと同じだけの計算処理が必要となってしまうので
    キューを利用すること
'''

from collections import deque

N = int(input())
Commands = list(input())

Answer = deque([str(N)])

for i in range(N-1,-1,-1): # 最後にjoin()を使って出力しやすいように文字列型で数値を格納している
    #print(i,Commands[i])
    if Commands[i] == "L":
        Answer.append(str(i))
    else:
        Answer.appendleft(str(i))

print(" ".join(Answer))