# ABC066 - C

# 要求されている処理をそのまま実装すると、計算に時間がかかりTLEになる
# 逆転処理を無視して配列内の並びを見ていくと、奇数番目の要素は右から、偶数番目の要素は左からappend()が行われているように見える
# この点に着目して両端キューというデータ構造を利用した実装を行うと高速に解を求めることができる

from collections import deque

n = int(input())
a = [int(x) for x in input().split()]
b = deque()

def foolish_code(a): # そのまま実装した場合のコード。TLEで不正解となる
    b = []
    for i in range(len(a)):
        b.append(a[i])
        b = b[::-1]
    print(" ".join([str(b[i]) for i in range(len(a))]))
    return 
#foolish_code(a)


# 奇数番目の要素は右から、偶数番目の要素は左から挿入していく
for i in range(len(a)):
    #print(i,a[i])
    if (i+1)%2 == 1:
        b.append(a[i])
    else:
        b.appendleft(a[i])

if n%2 == 1: # 要素数が奇数個の場合は最後に別途逆転処理を行う必要がある
    b.reverse()
    
b = list(b)  # 成型してから出力
print(" ".join([str(b[i]) for i in range(len(b))]))