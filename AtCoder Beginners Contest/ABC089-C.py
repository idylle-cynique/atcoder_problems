# ABC089-C

# 主に数学的知識を問う問題
# 組み合わせ候補数を求める問題だが、与えられる名前の数が多いので、そのまま愚直に全探索することはできない
# 条件を満たす要素を絞り込み、同じ頭文字をとる名前は一括して計算できるように組み合わせ公式を利用する必要がある

import collections, itertools

n = int(input())
s = set()

for i in range(n): # 頭文字がlist("MARCH")のいずれかである名前文字列のみを受け取る。
    tmp = input()
    if tmp[0] in list("MARCH"):
        s.add(tmp # 念のためset型に格納して重複している名前文字列にも対応できるようにしておく

initial_dict = {}
ans = 0

for i in "MARCH": 
    initial_dict[i] = 0

for name in s: # 受け取った名前リストから各頭文字をとる名前の数を調べる
    initial_dict[name[0]] += 1
#print(initial_dict)

name_initial = []
name_times = [] # 結局使わなかったので消してもよい
combi_list = []
    
for i,j in initial_dict.items():
    #print(i,j)
    if j != 0:
        name_initial.append(i)
        name_times.append(j)
        
#print(name_initial); print(name_times)

combi_list = list(itertools.combinations(name_initial,3)) # itertoolsライブラリを用いて組み合わせ列挙。最大でも5_C_3 = 10通りしかない

for combi in combi_list: 
    #print(combi) 
    tmp = 1
    for j in combi: # 組み合わせに対応する名前の個数から組み合わせ候補数を計算
        tmp *= initial_dict[j]
    ans += tmp

print(ans)

