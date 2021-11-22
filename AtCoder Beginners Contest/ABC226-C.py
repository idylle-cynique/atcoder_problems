# ABC226 - C

'''
早い話、N番目の魔法と、N番目の魔法を覚えるのに必要な魔法を覚えるのに掛かる時間はいくらか、
について問われている。また、入力サンプルでは分からないが、問題のポイントとなる部分として
「N番目の魔法の習得には必要ないが、N番目の魔法の習得に必要な魔法を習得するのに必要なX番目の魔法などが有り得る」
というのがある。このため、単にN番目の魔法で必要となる魔法の番号を参照するだけでは不十分で、
各番目の魔法をさらに参照して「N番目の魔法の習得に必要な魔法の習得に必要な魔法」まで脱漏なくリストアップする必要がある

そのためにはある魔法とその魔法の習得に必要な魔法の番号を隣接リストを用いてグラフ化し、
それをグラフ探索アルゴリズムを用いてN番目の魔法の習得に必要な魔法の番号から順番に全探索し
N番目の魔法の習得に必要な魔法をリストアップしていけばよい

ここでの実装では全探索に幅優先探索(BFS)を用いている
'''

from collections import deque

N = int(input())
T = [None,] # 各魔法を習得するのに必要な時間のリスト
Adj = [[] for _ in range(N+1)] # 隣接リスト
time = 0

for i in range(N):
    tmp = list(map(int,input().split()))
    T.append(tmp[0]) # 習得に必要な時間のリスト
    Adj[i+1] = tmp[2:]
    if i == N-1:     # N番目の魔法については、別途リストにも格納
        Need = tmp[2:] + [i+1] 
#print(Adj); print(Need)

def BFS(): # 幅優先探索によるグラフ全探索
    queue = deque(Need) # N番目の魔法の習得に必要な魔法のリストをキューに格納
    visited = [False] * (len(Adj)) # 探索済みの有無を記録
    check_list = set(Need) # 魔法の習得に必要な魔法のリスト

    while(len(queue) != 0):
        v = queue.popleft()
        #print(v,":",Adj[v])
        for ele in Adj[v]:
            if visited[ele] == False: # 未探索の魔法
                queue.append(ele)   # キューに番号を格納
                check_list.add(ele) # チェックリストにリストアップ
                visited[ele] = True # 探索済みに変更
    return check_list # チェックリストを返す

Magics = BFS() #;print(Magics,T)

for magic in Magics:
    time += T[magic]

print(time)