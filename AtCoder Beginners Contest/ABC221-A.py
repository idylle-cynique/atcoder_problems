''' ABC221 - A
問題文から分かるように、32^A ÷ 31^B = 32^(A-B)をそのまま求めるだけでよい
'''

A,B = map(int,input().split())
print(32**(A-B))