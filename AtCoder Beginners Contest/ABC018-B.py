''' ABC018 - B
    そのまま実装するだけでよい問題
    この実装では入力値の文字列の長さとクエリの処理回数によっては計算時間が膨大になるが
    ここでの文字列の長さは最大でも100と非常に短いので、そのまま愚直な実装を行うだけでも
    全く問題なくAC判定が得られる
'''

String = list(input())
N = int(input())

for i in range(N):
    l,r = map(int,input().split())
    tmp = String[l-1:r]
    String[l-1:r] = tmp[::-1]

print("".join(String))