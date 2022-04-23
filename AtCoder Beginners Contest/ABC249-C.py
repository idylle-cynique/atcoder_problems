''' ABC249 - C
    Nの制約が小さいことに着目して、全探索する方法を考える
    与えられた文字列群のうちから何個取り出してもいい、というところを考えると
    各文字列要素を「使う・使わない」の2パターンで管理し適時取り出すbit全探索がおあつらえ向き、
    と考えることができる。

    そのほかの部分についてはそのまま問題で要求されている処理を
    そのまま何かしらの手段で実現しさえすればよく、計算にあたって工夫する必要はない
'''

N,K = map(int,input().split())
Strings = [input() for x in range(N)]

pattern = 2**N # 全部で2^N通りの選び方がある
answer = 0

for i in range(1,pattern):
    alphs_counter = dict()
    for j in range(N): 
        if (i>>j)&1: # 右シフト演算して1が得られた桁番号の文字列要素を取り出す
            # 取り出した文字列要素中の文字(英小文字)の出現回数を辞書に記録していく
            for c in set(Strings[j]):  
                if c in alphs_counter:
                    alphs_counter[c] += 1
                else:
                    alphs_counter[c] = 1
    
    #print(alphs_counter)
    cnt = 0
    for v in alphs_counter.values(): # 出現回数がKである文字が何個存在するか調べる
        if v == K:
            cnt += 1
    
    answer = max(answer,cnt) # 最高値を更新
    
print(answer)
        