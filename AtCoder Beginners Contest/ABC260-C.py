''' ABC260 - C
    問題文で要求されている処理をそのまま実装すればよい
    解説では動的計画法～などと書かれているが、特段複雑な実装を行うものではない

    イメージとしては、フィボナッチ数列におけるN番目の値を求める～といったような処理を
    下からではなく上から行うような具合

    なお、ここではインデックスとレベル値とがそのまま対応するように、
    リストではなく辞書(dict)を用いて実装を行っているが、特に実装内容に差はない
'''

N,X,Y = map(int,input().split())

Reds = dict({n:0 for n in range(1,N+1)})
Blues = dict({n:0 for n in range(1,N+1)})
Reds[N] = 1
#レベルn の赤い宝石 (n は 2 以上) を「レベル n−1 の赤い宝石 1 個と、レベル n の青い宝石X個」に変換する。
#レベルn の青い宝石 (n は 2 以上) を「レベル n−1 の赤い宝石 1 個と、レベル n−1 の青い宝石Y個」に変換する。
flag = True
red_flag = True
blue_flag = True

while(flag):
    for level,number in Reds.items():
        if level>1 and number>0:
            Reds[level-1] += (number)
            Blues[level] += (number*X)
            Reds[level] = 0
            break
    else:
        red_flag = False
    
    for level,number in Blues.items():
        if level>1 and number>0:
            Reds[level-1] += (number)
            Blues[level-1] += (number*Y)
            Blues[level] = 0
            break
    else:
        blue_flag = False
    
    if not(red_flag or blue_flag):
        flag = False
    else:
        red_flag = True
        blue_flag = True

print(Blues[1])