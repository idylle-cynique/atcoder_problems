''' ABC088 - D
    幅優先探索アルゴリズムの実装を求める問題
    黒く塗るマスの数を最大化させるためには、白いままにしておくマスの数を最小化させなくてはならない
    また白いままにしておくマスの数を最小化させるためには、左上から右下まで最短で到達する必要がある
    すると、幅優先探索を用いて右下へ到達するまでの最短距離(最低限必要なマスの数)を求め、
    それをグリッド全体の白いマスの数から差し引いた分が解となる
'''

from collections import deque
from copy import deepcopy

H,W = map(int,input().split())
Grid = []
distmap = [[-1 for i in range(W+2)] for j in range(H+2)]
white_cnt = 0
dy = [-1, 0,+1, 0]
dx = [ 0,+1, 0,-1]

for i in range(H+2): # グリッド情報を受取
    if i == 0 or i == H+1:
        Grid.append(list("x"*(W+2)))
    else:
        Grid.append(list("x" + input() + "x"))

for j in range(H+2): # 距離情報を格納するためのマップを生成
    for i in range(W+2):
        if Grid[j][i] == "x":
            distmap[j][i] = H*W
        elif Grid[j][i] == "#":
            distmap[j][i] = H*W
        else:        # ついでに白いマスの数も数え上げておく
            white_cnt += 1

def view_grid(field): # グリッド情報を確認
    for row in field:
        print("".join(row))
    return True

def view_distmap(distmap):
    for row in distmap:
        print(row)
    return True

def Grid_BFS(field,x,y):
    ny,nx = y,x
    distmap[ny][nx] = 0
    d = 0
    #field[ny][nx] = "*"
    search_queue = deque([[1,1,0]]) # スタート位置の情報を探索キューに格納
    
    while(len(search_queue) != 0): # 探索すべきマスが存在しなくなるまで幅優先探索
        #print(search_queue)
        ny,nx,d = search_queue.popleft() # 探索キューから探索を行うマスの座標とスタート位置からの距離(d)を得る
        #field[ny][nx] = "*"
        d += 1
        for k in range(len(dx)):
            y,x = ny+dy[k],nx+dx[k]
            if distmap[y][x] == -1: # 未訪問のマスなら探索キューに格納
                search_queue.append([y,x,d])
                distmap[y][x] = d   # 距離情報をdistmapに与える
    
    return field

field = deepcopy(Grid)
field = Grid_BFS(field,1,1)
#view_distmap(distmap)

if distmap[H][W] == -1: # ゴール(右下)に到達できなかった場合
    print(-1)
    exit()
else:                   # ゴールに到達出来た場合
    #print(white_cnt,distmap[H][W])
    print(white_cnt - (distmap[H][W] + 1))

