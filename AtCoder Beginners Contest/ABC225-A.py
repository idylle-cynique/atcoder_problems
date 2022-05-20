''' ABC225 - A
    実際に組み合わせ列挙などを行ってもよいが、
    組み合わせ数自体は単に、対象の文字列中に用いられている文字の種類数さえ
    分かれば計算して求めることができるので、そちらを使って解いた方が良い
    早い話数学問題で、「同じものを含む順列の総数」などと呼ばれているもの

    ここでは直接値を与えてしまっているが、意味としては以下の通り
        1) 使われている文字の種類が1種類なら、作れる文字列は 3!/3! = 1通り
        2) 使われている文字の種類が2種類なら、作れる文字列は 3!/2!・1! = 3通り
        3) 使われている文字の種類が3種類なら、作れる文字列は 3!/1!・1!・1! = 6通り
'''

S = input()
S_set = set(list(S))
#print(S_set)

if len(S_set) == 1:
    print(1)
elif len(S_set) == 2:
    print(3)
else:
    print(6)