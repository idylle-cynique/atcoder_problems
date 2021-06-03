# ABC158 - D

# 処理に用いるデータ構造としてキュー(queue)を利用する必要がある
# 反転処理については、他の類題と同様実際に反転処理を行うのではなく、
# 反転状態にあるかどうかだけを記憶してそれに応じた文字の追加処理を行うようにすること

from collections import deque
from copy import deepcopy 

S = deque(input())
N = int(input())
r = False # 反転処理フラグ

string = deepcopy(S)
#print(string)

for i in range(N):
    tmp = list(map(str,input().split())) # list(input().split())などとしてWAを連発させてしまったので、以後は必ずmap()を使うこと
    t = int(tmp[0])
    
    if t == 1:  # T = 1 なら反転フラグの論理値を入れ替える
        r = not r
    else:       # T = 2 なら文字の追加処理を行う
        f,c = int(tmp[1]),tmp[2]
        #print(":",t,f,c);
        if f == 1: 
            if r == True: # 反転時に先頭に追加なら、末尾に追加
                string.append(c)
            else:         # 通常時に先頭に追加なら、そのまま先頭に追加
                string.appendleft(c)
        else:
            if r == True: # 反転時に末尾に追加なら、先頭に追加
                string.appendleft(c)
            else:         # 通常時に末尾に追加なら、そのまま末尾に追加
                string.append(c)

string = list(string)

if r == True: # 反転フラグがTrueなら最後に反転させる
    string = string[::-1]

print("".join(string))