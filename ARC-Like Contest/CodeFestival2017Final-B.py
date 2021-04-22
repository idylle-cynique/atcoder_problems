# CODE FESTIVAL 2017 FINAL - B

import collections

# 3種類の文字しか使わない、という制約の中で回文文字列を避けるにはXYZXYZ...のような(XYZ)パターンを繰り返す方法しかない
# すべての文字が同じ数だけ揃っていない場合でも末尾を XYZX, XYZXYのような形に留められるなら回文は回避可能

# コーナーケースとして
# (1) 与えられた文字の種類が1つのとき
# (2) 与えられた文字の種類が2つのとき
# があり、これらは可―不可の判別プロセスを別途考える必要があるので注意すること

s = input()
s_data = collections.Counter(s)
alphs = []
alph_min = 10**5
alph_max = 0
#print(s_data)

for k in s_data.values(): # 各文字の個数データの取り出し、最多数、最少数の確認
    if k > 0:
        alphs.append(k)
        
    if alph_min > k: 
        alph_min = k
        
    if alph_max < k:
        alph_max = k
        
#print(alphs); print("min:",alph_min); print("max:",alph_max);

if len(alphs) == 1: # 与えられた文字の種類が1つのとき
    if alphs[0] == 1:
        print("YES")
    else:
        print("NO")
    exit()

if len(alphs) == 2: # 与えられた文字の種類が1つのとき
    if sum(alphs) == 2:
        print("YES")
    else:
        print("NO")
    exit()

if alph_max-alph_min >= 2:
    print("NO")
else:
    print("YES")