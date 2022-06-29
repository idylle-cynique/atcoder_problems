''' ABC257 - B
    問題で要求されている処理をそのまま実現することで正答が得られる問題
    問題中における各順番のコマの位置を都度把握しながら移動させる、というところが
    やや手間のかかるところではあるが、マスの数Nは最大200とさして多くなく
    またクエリ処理回数Qも最大で1000なので
    i番目のコマの位置を線形探索で確認するような愚直な実装方法でも
    十分高速に処理できるであろう、と推察される

    とはいえ、このような実装を取るのは当然ながら望ましくないので、各番目のコマの位置を
    辞書コンテナ(C++におけるunorderd_map)に格納し、これを参照・更新することで
    各コマの位置情報の取得処理をO(1)で行っている

    この場合ではクエリ処理回数分だけのループで済むので、
    愚直な実装での計算量O(N・Q)に対してO(Q)と断然計算量を抑えることができる
'''

N,K,Q = map(int,input().split())
A = [int(x) for x in input().split()]
L = [int(x) for x in input().split()]

pieces = dict()
field = list([0 for x in range(N+1)])

for i,a in enumerate(A):
    pieces[i+1] = a-1
    field[a-1] = 1

for q in L:
    if field[pieces[q]+1] or pieces[q] == N-1:
        pass
    else:
        field[pieces[q]] = 0
        field[pieces[q]+1] = 1
        pieces[q] += 1

answer = list()
for idx in range(N):
    if field[idx]:
        answer.append(str(idx+1))

print(" ".join(answer))

