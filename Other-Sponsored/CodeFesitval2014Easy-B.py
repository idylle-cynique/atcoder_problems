# Code Festival 2014 Easy - B

'''
    順位を40位ごとに区切り、順位に対する40との剰余値を用いて計算すればよい
    40位区切り程度なら全パターン列挙することも容易なので、辞書型などを用いて
    グループ分けのパターンを事前に用意して割り振るのもよい
'''

N = int(input())

mod40 = N%40 
if mod40 == 0:
    print(1)
elif mod40 <= 20:
    print(mod40)
else:
    print(41-mod40)