# ARC086 - C

# 数列aに出現する要素と、各要素の出現回数をまとめ、出現回数の少ない要素から書き換えて行けば最適解が求められる
# 数列aの整理には collecitons.Counter() を利用する方法もある

n,k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
a_dict = {}

for i in range(n): # 出現した要素とその要素の出現回数を辞書型でまとめる
        if a[i] not in a_dict:
                a_dict[a[i]] = 1
        else:
                a_dict[a[i]] += 1
#print(a_dict)

if len(a_dict) <= k:
        print(0)
        exit()
        
as_dict = sorted(a_dict.items(), key=lambda x:x[1]) # 出現回数の少ない要素順にソートされた二次元リストを作る
tmp = len(as_dict)
ans = 0

for i in range(len(as_dict)):
        ans += as_dict[i][1]
        tmp -= 1
        #print(as_dict[i][1]); print("tmp:",tmp,"k:",k)
        
        if tmp <= k:
                print(ans)
                break