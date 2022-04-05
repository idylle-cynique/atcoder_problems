# ABC242 - C

'''
    問題文に、条件を満たす数の個数は大きくなる可能性があるので、余り値を解とする、と
    なっていることからも推察される通り、実際に条件を満たす数の数え上げるような処理では計算が間に合わない
    何かしらの規則性を見つけて、条件を満たすものの個数をざっくり数え上げるようなやり方が求められている

    そこで、条件を満たすような数字を自分の手で紙などに書き出してみると、
    桁数がXの条件を満たす数からX+1桁の条件を満たす数は、次のような法則によって求められることがわかった

    1) X+1桁の条件を満たす数のうち、末尾に1の値が付けられるのは
        i) X桁の条件を満たす数のうち、末尾が1であるもの
        ii)X桁の条件を満たす数のうち、末尾が2であるもの
        の数だけある
    2) X+1桁の条件を満たす数のうち、末尾に9の値が付けられるのは
        i) X桁の条件を満たす数のうち、末尾が8であるもの
        ii)X桁の条件を満たす数のうち、末尾が9であるもの
        の数だけある
    3) X+1桁の条件を満たす数のうち、、1),2)以外の値が末尾につくものはX桁目の値をYとしたときに
        i)  X+1桁目の末尾が Y-1 であるもの
        ii) X+1桁目の末尾が Y であるもの
        iii)X+1桁目の末尾が Y+1 であるもの
        の数だけある
    
    あとはこの法則性を踏まえて、
    「i桁目の数で条件を満たすもの」の個数と、i-1桁目の末尾がnで条件を満たすものの数を個別に
    配列や辞書などに記録しておき、それを更新していくことで問題の答えを高速に求めることができる
    解説とは少し解法が異なるが、概ね解説におけるDPテーブルによる解法の方針に近い

    また、これらの値のインクリメント処理に際しては、その都度余り値への変換を行い
    和算処理を可能な限り単純（小さな値の和算）にするようにしたほうがよい
    Pythonの場合はそのままでもひとまず計算処理自体は可能だが、C++などの言語では
    事前に定めた型で取り扱える範囲を超えてしまう(32bitの符号なし整数では収まらない)場合がある
'''

N = int(input())
Numbers = [[1 for n in range(10)] for _ in range(2)]
cnt = 1
MOD = 998244353 

for i in range(1,N):
    for i in range(1,10):
        Numbers[0][i] = Numbers[1][i]
    total = 0
    for key in range(1,10):
        if key == 1 or key == 9:
            if key == 1:
                Numbers[1][1] += Numbers[0][2]
            else:
                Numbers[1][9] += Numbers[0][8]
        else:
            Numbers[1][key] += Numbers[0][key-1]
            Numbers[1][key] += Numbers[0][key+1]
        Numbers[1][key] %= MOD
        total += Numbers[1][key]
    
    cnt = total
    cnt %= MOD
    #print(cnt,Numbers[1][1:])

print(cnt)