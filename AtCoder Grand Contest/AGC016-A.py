# AGC016 - C

# 処理の内容が若干入り組んでおり掴みにくいが、制約が |S| = 100 と小さいので効率的な探索手段を考える必要はなく
# そのまま入力文字列中の各文字で処理を実現した場合の必要処理回数を全探索で求め、その中から最小回数となるものを記憶すればよい
# |S| = 100 の場合でも O(N^3) ≒ 10**6回程度のループ処理で終えられるので、確実に 2000ms 以内に処理を終えることができる
# ただし実際の処理を行うとき、入力文字列からのコピーは代入処理ではなく、copyモジュールを用いて深いコピーを行う必要があることに注意すること

from copy import deepcopy
from collections import Counter

S = input()
ans = 100 # 解(処理を終えられる最小回数)を記録

for c in S: 
    string = list(deepcopy(S)) # deepcopyで入力文字列を受け取る
    base = c # 単一化させるにあたってベースとなる文字を得る 
    cnt = 0  # 問題の処理を実現するのに必要な処理回数を記録
    #print(S,"- base_chara:",c)
    while(len(set(string)) != 1): # 単一文字からなる文字列になるまで処理
        tmp = deepcopy(string)    # 実際に処理を行う文字列 

        for i in range(len(tmp)-1): # 問題の処理を実際に行っていく
            if (string[i+1] == base): # 対象の文字が現れたらその文字に置き換える
                tmp[i] = base
                tmp[i+1] = base
        
        tmp.pop() 
        string = deepcopy(tmp) # 末尾を取り除いて再び次のループ処理へ
        cnt += 1
        #print(cnt,":","".join(string))
        
    ans = min(ans,cnt)

print(ans)