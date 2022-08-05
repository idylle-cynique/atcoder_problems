''' ABC256 - D
    Union～と題された問題だが、UnionFindTreeを解法に用いるわけではない
    一連の半開区間の情報を整理して最小の個数の右半開区間を求めよ、
    というピンとこない書かれ方をしているが、要するに
    半開区間として示されている区間で統合可能なものは全て接続して、
    簡潔な区間情報に直して出力せよ、ということ

    問題の核としては ABC221-D のような問題と同じで、
    ある区間における入と出の部分の情報だけを取り挙げ累積和のようなやり方で処理してやることで
    問題で求められているような処理を実現することができる

    こうした問題を解く際に用いられているアルゴリズムは、一般にimos法(いもす法)と呼ばれる
    ABC221-Dと異なり今回の問題では数直線のx座標の最大値が2*10^5と線形探索が可能な程度の長さなので
    実際に配列やリストを使って数直線を再現する方法もあるが、ここでは重複区間(統合可能な区間)が
    多い場合に必要記憶領域を削減できるよう、辞書(dict)を使って入と出の部分の情報のみを記録したあと
    昇順に各入・出の要素を取り出してカウンタを回し、
    カウンタが0になった時点で統合を開始した左地点とその時点でいる地点とを記録し
    answerリストに格納していく、というやりかたを取っている
'''

N = int(input())
intervaldict = dict()
coordinates = list()
for _ in range(N):
    x,y = map(int,input().split())
    if x not in intervaldict: intervaldict[x] = +1
    else:                     intervaldict[x] += 1
    if y not in intervaldict: intervaldict[y] = -1
    else:                     intervaldict[y] -= 1 

for k,v in intervaldict.items():
    coordinates.append([k,v])

coordinates.sort()
counter = 0
sx = 0
answers = list()

for element in coordinates:
    x,f = element
    if not(counter): sx = x
    counter += f

    if counter == 0:
        answers.append([str(sx), str(x)])

for ans in answers:
    print(" ".join(ans))