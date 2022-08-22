''' ABC082 - C
    良い数列を作るために出来る処理は、ある要素を取り除くことだけなので、
        1) ある要素xがx個未満の時は、値がxである要素をすべて取り除く
        2) ある要素xがx個よりも多い時は、余っている要素分だけ取り除く
        3) ある要素xがちょうどx個の時は、何もしない
    といった具合に処理するだけでよい
    これらの処理はO(N)で行えるので、実行時間制限にかかることもない
'''

from collections import Counter

N = int(input())
nums = [int(x) for x in input().split()]
nums_data = Counter(nums) # 得た数列の中身をcollections.Counterで整理
ans = 0

for k,v in nums_data.items():
    #print(k,v)
    if k > v:     # 整数要素それ自体よりも個数が少ない時は、全て取り除く
        ans += v
    elif k < v:   # 整数要素それ自体よりも個数が多い時は、余分な分だけ取り除く
        ans += (v-k)
    else:         # ちょうどあるなら何もしない
        pass

print(ans)