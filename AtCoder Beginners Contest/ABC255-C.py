''' ABC255 - C
    例題を実際に手を動かして計算してみると特にループ処理などを用いなくても
    概ね解となるような値がどんなものになるか見当がつくことがわかる

    これを上手く場合分けを用いながら整理しつつ、計算で解を求めるようにしていけばよい

    具体的には、まずXが数列中の値の範囲外であるようなとき
        i)  数列中の最小値よりもXが小さい
        ii) 数列中の最大値よりもXが大きい
    この場合、Xを数列の最小値ないし最大値までの差分を埋めるのに必要な操作回数が解となる

    それ以外、Xが数列中の値の範囲内に収まるようなときは
    数列の初項が0とし、その相対差が一致するようにXの値を調整後
        i)  数列中の要素でX以下の値のうち最も差が小さい要素
        ii) 数列中の要素でX以上の値のうち最も差が小さい要素
    の2つのうち、より操作回数(差の絶対値)が小さいものが解となる

    このときのi), ii)の具体的な値を求める方法については、
    上記の調整後のXを等差で割ってやれば最も近い値の項数(何項目か)が分かり
    次のような式でi),ii)の二つの値が得られる
        i)  D*((X-A)//D) 
        ii) D*((X-A)//D+1)
    この2つのうち最小を取るものが解となる

    なお以下の実装では中途の値を見ながら計算をするため、複数の変数を用いて分割して計算している
'''

X,A,D,N = map(int,input().split())
number = (N*D)+A

answer = 0

if D >= 0: 
    max_member = A+D*(N-1)
    min_member = A
else:
    max_member = A
    min_member = A+D*(N-1)

if min_member < X and X < max_member:
    base_num = X-A
    base_div = base_num//D
    next_member = D*(base_div+1)
    prev_member = D*base_div
    answer = min(abs(prev_member-base_num), abs(next_member-base_num))
    #print(X,prev_member,next_member, base_num, answer)  
else:
    answer = min(abs(X-min_member), abs(X-max_member))

print(answer)

