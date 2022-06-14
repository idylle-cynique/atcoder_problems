""" ABC006 - B
    問題そのものの解説についてはC++による解答コードファイルに記載
    C++での解答ではメモ化再帰による上からのDPを用いたが、Pythonの場合では
    200,000程度の番目のトリボナッチ数を求めようとした辺りからメモリを過大に占有し
    ランタイムエラーや制限メモリ量の超過を起こし、正答を得ることが出来なかった
    そのためforループにより下からの実装とした

    Pythonでこのような結果となった理由として、おそらく動的型付けかつ多倍長整数が取り扱い可能な
    代償として、C++などの静的型付けかつ固定長での値の格納をベースにした言語と異なり値の格納に際して
    占有するメモリ量がかなり大きいことがあると思われる

    基本的な計算量が変わらなくとも、その処理過程で必要とするリソースが膨大になることで
    処理効率が大きく悪化する場合があるという好例ではないか
"""

N = int(input())
MOD = 10007
tribonacci = list()
initial_values = [0,0,1]

for n in initial_values:
    tribonacci.append(n)
    
for i in range(N-len(initial_values)):
    tribonacci.append((tribonacci[-1] + tribonacci[-2] + tribonacci[-3])%MOD)

answer = tribonacci[N-1]
print(answer)


