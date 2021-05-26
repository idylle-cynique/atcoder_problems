# JSC2021 - C

# 妙に詰まった問題(解説AC)
# 問題文をそのまま解釈して最小公倍数をうまく求めようとするのではなく、
# 答えを N であるとして、それは指定された条件(A以上B以下である数から2つ選んだ時に得られる数か)を満たすか……
# という逆の発想で考える必要があり、実際に最小公倍数アルゴリズムを駆使する必要はないし、駆使してはいけない

# A以上B以下の数にNの倍数(約数にNを持つ数)が何個あるかは
# (1～Bまでに含まれるNの倍数の数) - (1～(A-1)までに含まれるNの倍数の数) とすることで求めることができる。
# Nの倍数が2つ以上あればNは問題の解としての条件を満たす。Nであり得る値のうち一番大きいものを求めたいので
# 大きい方(B-1)から探索を開始して、一番最初に解としての条件を満たす値を出力すればよい
# コード自体は単純だが、問題文を読み替えて得たい解を求める手段を思いつくまでが難しい

A,B = map(int,input().split())

for n in range(B-1,0,-1):
    #print(n,B//n,(A-1)//n,":",B//n - A//n)
    if (B//n) - ((A-1)//n) >= 2:
        print(n)
        break