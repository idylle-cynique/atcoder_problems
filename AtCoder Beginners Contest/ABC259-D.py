''' ABC259 - D
    まず問題の内容、各円の演習を通って指定した座標から別に指定した座標へと移動する
    という処理をどのような形でプログラムに落とし込むか、というのが問題となる

    これが単なるグリッドマップやグラフ理論にしたがって表現されたリストなどであれば
    単なる基礎的な探索アルゴリズム問題と解釈して解くことができるので、
    どうにかして各円の通路(円周)の接続関係を整理して隣接リストで表せないか考えてみる
    ことが実装の出発点となる

    円が接続しているかどうかというのは、入力として与えられた円のうちの
    ある円とある円とが2点ないし1点で接しているかどうか、ということと同じ意味である

    これは高校数学(数B)などでやったように、円が接しているか否かは、
    2つの円の中心座標におけるユークリッド距離dと2つの円の半径r_1,r_2を用いて判定することができる
    2つの円が接するのは
        i)   d = r_1 + r_2 (外接するとき)
        ii)  d < r_1 + r_2 (2点で交わるとき)
        iii) d = |r_1 - r_2| (内接するとき)
    なので、これらの条件のいずれかを満たす2円は接続関係(行き来可能)にあるとみなせる

    あとはこれを、浮動小数点数計算などによる誤差などを発声させないように計算しながら実装し、
    各円の接続関係を隣接リストの形で表現する

    あとはグラフ探索アルゴリズムのひな型に
    隣接リスト、スタート位置に相当する円、ゴール位置に相当する円とを与えてやればこの問題における
    解が求められる

    解として出力したいのは単に行き来可能かどうかの情報だけで、最短距離などではないので
    利用するグラフ探索アルゴリズムはDFS、BFSのいずれであってもよい

    各種処理の計算量は
        i)   スタート位置にあたる円、ゴール位置にあたる円がN個の円のうちのどれであるかを求めるのに O(N)
        ii)  N個のうちのすべての2円の組み合わせの接続関係を調べるのに O(N^2)
        iii) 生成された隣接リストの探索に O(N^2)
    で、全体では O(N^2)
    Nの制約は最大3000なので、この計算量でも十分高速に処理が可能である

    が、Pythonの場合実行時コンパイル機能のあるPyPyで提出しないとTLEになるので注意が必要
    これが原因でコンテスト時間内のACを逃したので、Pythonでグラフ探索系の処理を行う場合は
    計算量に関係なくPyPyで提出するのが望ましい    
'''

from collections import deque
import math

N = int(input())
sx,sy,gx,gy = map(int,input().split())
coordinates = [[0,0,0] for x in range(N)]

Adj = [list() for n in range(N)]

for idx in range(N):
    tx,ty,tr = map(int,input().split())
    coordinates[idx] = tx,ty,tr

#print(coordinates); print(adj_list)

for i in range(0,N):
    for j in range(i+1,N):
        ax,ay,ar = coordinates[i]
        bx,by,br = coordinates[j]
        
        # 二点間のユークリッド距離が二円の半径の和よりも等しい、もしくはそれより小さいなら、交点をひとつ以上持つ
        # すなわち、二点間は行き来が可能である、ということになる
        
        ed = (bx-ax)**2 + (by-ay)**2
        #print(ed, "<=", ar+br,"?")
        
        if not(ed>(ar+br)**2 or ed < abs(br-ar)**2):
            #print(f"{i}番目,{j}番目の円は行き来可能")
            Adj[i].append(j)
            Adj[j].append(i)

start = -1
goal = -1

for idx in range(len(coordinates)):
    x,y,r = coordinates[idx]
    #print(x,y,r)
    # 座標が円周上にあるかどうかチェック
    # 二点間のユークリッド距離が半径に等しければ円周上にあると言える(必ず整数値ベースで計算)
    if (x-sx)**2 + (y-sy)**2 == r**2:
        start = idx
    
    if (x-gx)**2 + (y-gy)**2 == r**2:
        goal = idx


def BFS(): # 幅優先探索(BFS)のひながた
    queue = deque([start])
    visited = [False] * (len(Adj))
    visited[start] = True

    while(len(queue) != 0):
        v = queue.popleft()
        for ele in Adj[v]:
            if visited[ele] == False:
                queue.append(ele)
                visited[ele] = True
    return visited

#print(Adj,start,goal)
reachable_positions = BFS()
#print(reachable_positions)

if reachable_positions[goal]:
    print("Yes")
else:
    print("No")