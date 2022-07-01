''' ABC253 - A
    入力値をソートして中央の番目の値(2番目)の値を出力すればよい
'''
a,b,c = map(int,input().split())
abc = sorted([a,b,c])

if abc[1] == b:
    print("Yes")
else:
    print("No")