# ABC244 - C

'''
    対話形式での処理を求める問題
    過去にARCなどで出題されたことのある形式だったとのことだが、
    自分がABCに参加を開始して移行ではおそらく初めて

    あくまでも対話式で動的に入力値が変化する、というだけでそれ以外に大きな変化はないが
    実装を間違えた際の判定が通常と異なるので注意が必要となる

    問題で期待される処理をそのまま実装するだけでよい
    制約がN=1000と、出力に利用できる数値の検索を線形探索で行っても問題ない範囲で
    設定されているので、愚直な探索法をベースに全体でO(N^2)となるような効率の悪い実装でも
    容易に正答が得られる
'''

Number = int(input())
availableNumbers = set([int(x) for x in range(2,2*Number+1+1)])
takahashi = 1
aoki = -1
print(1)

while(True):
    aoki = int(input())

    if aoki == 0:
        exit()

    availableNumbers.discard(aoki)
    takahashi = availableNumbers.pop()
    print(takahashi,flush=True)