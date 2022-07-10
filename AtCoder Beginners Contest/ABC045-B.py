# ABC045 - B

# 問題文の処理をそのまま実装すればよい問題
# ここでは問題文により忠実になるようにという意図でカードを格納するためのデータ構造としてdequeを用いているが
# カードの取り出しは先頭のみからしか行われないので、「カードの並びを逆にして、末尾から取る」という発想を取れば
# A_card.reverse()で反転, A.pop()で先頭のカードを取り出す、という形で、dequeを用いず通常のリストで実装できる

from collections import deque

A_card = deque(input())
B_card = deque(input())
C_card = deque(input())

winner = None
poped_card = None

while(winner == None): # 勝者が決まるまでゲームを続行
    if poped_card == None: # 初回処理
        poped_card = A_card.popleft()
        continue
    #print(":",poped_card); print(A_card,B_card,C_card);
    
    if poped_card == "a":   # 取り出されたカードが a
        if len(A_card) == 0: # 持ち手札がなくなったら勝利
            winner = "A"
            break
        poped_card = A_card.popleft()
    elif poped_card == "b": # 取り出されたカードが b
        if len(B_card) == 0: # 持ち手札がなくなったら勝利
            winner = "B"
            break
        poped_card = B_card.popleft()
    else:                   # 取り出されたカードが c
        if len(C_card) == 0: # 持ち手札がなくなったら勝利
            winner = "C"
            break
        poped_card = C_card.popleft()

print(winner)