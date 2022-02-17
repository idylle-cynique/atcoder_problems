# ABC231 - D
'''
 まず問題内容を整理し、具体的にどのようなデータ構造に直して取り扱えばいいかを考える
 「人A_iと人B_iが隣り合っている」という状態は隣接リストと無向グラフの関係として捉えることができる
 「横一列に並べることができる」と言える状態は、得られた隣接リストが
 (1) 3つ以上の辺(隣り合う人間が三人以上)がない
 (2) 2つからなる辺のうち、ループ(閉路)を形成するような要素(円状に隣り合う人たち)がない
 の2つの条件を充たすような隣り合いかたをしているときだと言える
 あとはこれを実装すればよい。この2つの条件のうち(2)については、さらに
 「(1)を充たす隣接リストに対して幅優先探索を行った場合に、どの地点からも未到達の地点(人)が一度に2つ検出されることがない」
 というふうに言い換えることができ、この処理を幅優先探索アルゴリズムに組み込み、条件を充たさない隣接リストを弾いている
'''

from collections import deque

N,M = map(int,input().split())
Adj = [[] for _ in range(N)]
visited = [False] * (len(Adj))
queue = deque()

for i in range(M):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    Adj[a].append(b)
    Adj[b].append(a)

def BFS(): # 幅優先探索(BFS)のひながた
    while(queue):
        v = queue.popleft()
        cnt = 0
        for ele in Adj[v]:
            if visited[ele] == False:
                queue.append(ele)
                visited[ele] = True
            else: # 一度に2つの未到達地点が形成された場合、その隣接リストは閉路(ループ)を含んでいるので横一列に並べることはできない
                cnt += 1
                if cnt >= 2:
                    print("No")
                    exit()
    return True

for route in Adj: # 得られた隣接リストに3つ以上の辺を持つ要素が見つかった場合、それは横一列に並べることはできない
    #print(route)
    if len(route) > 2:
        print("No")
        exit()
    else:
        pass

for point in range(N):
    #print(point,visited[point])
    if visited[point] == False:
        queue.append(point)
        visited[point] = True
        BFS()

print("Yes") # 弾かれることなく一連の処理を終えた場合、それは横一列に並べることができる隣接リストだと言える