# ZONe2021 - D

# そのままリストによる実装を行うとreverese()処理を要求されるごとに行うと一回ごとにO(N)もの計算を要してしまう
# これを避けるためには、リスト反転時の文字追加処理を両端キューのappendleft()を用いる必要がある
# このほか、連続した同じ文字二文字の削除処理は問題文の通りに文字追加処理後に別途行おうとすると一部の問題ではTLEとなってしまうようだったので
# 文字追加処理中に同時進行で行うものとした

from collections import deque

S = input()
DE_Queue = deque()
rev = False

for i in S:
    if i == "R": # reverse()処理命令が来た？
        rev = bool((int(rev)+1)%2) # 反転処理フラグが TrueならFalse に、 FalseならTrue に切り替える
        continue
    
    if rev == True: # 反転時ならappendleft()で文字を追加
        DE_Queue.appendleft(i)
    else:           # 通常時ならappend()で文字を追加
        DE_Queue.append(i)
    
    if len(DE_Queue) < 2: # 両端キューの長さが2未満なら以下の処理は行わずに次のループへ
        continue
    
    if rev == True and DE_Queue[0]==DE_Queue[1]: # 反転時に先頭二文字が同じならその2つを削除
        DE_Queue.popleft()
        DE_Queue.popleft()
    elif DE_Queue[-1] == DE_Queue[-2]:           # 通常時に末尾二文字が同じならその2つを削除
        DE_Queue.pop()
        DE_Queue.pop()


if rev == True: # 反転フラグがTrueならreverse()で元に戻す
    DE_Queue.reverse()

print("".join(DE_Queue))