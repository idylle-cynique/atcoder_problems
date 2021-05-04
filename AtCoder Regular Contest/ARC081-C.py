# ARC081 - C

# (1) 長方形を作るためには 異なる長さの辺2つずつの計4つ、もしくは同じ長さの辺4つが材料として必要
# (2) 面積の大きな長方形を作るためには可能な限り長さの大きい辺を用いる必要がある
# 上の2点を踏まえたうえでその通りに実装を行えばよい

from collections import Counter

N = int(input())
Sides = [int(x) for x in input().split()]
sides_data = Counter(Sides) # ある長さの辺がいくつあるか、を調べる
sides_list = [] # 長方形を作るのに利用できる辺を格納しておく

for k,v in sides_data.items(): # 2つ以上の個数を用意できる辺だけを抜き出してリストに格納
    #print(k,v)
    if v >= 2:
        sides_list.append((k,v))

second = first = (0,0) # 一番目に大きい辺の長さと個数、二番目に大きい辺の長さと個数を格納

for k,v in sides_list:
    if first[0] < k:
        second = first
        first = (k,v)

#print(first,second)     

if first[1] >= 4: # 一番大きい長さの辺で正方形が作れる場合もある
    print(first[0]*first[0])
else:
    print(first[0]*second[0])