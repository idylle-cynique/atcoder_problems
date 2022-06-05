''' ABC217 - A
    文字列に大しても辞書順による大小比較が可能なので
    そのまま比較演算子を用いて比較すればよい
'''

S,T = map(str,input().split())

if S < T:
    print("Yes")
else:
    print("No")