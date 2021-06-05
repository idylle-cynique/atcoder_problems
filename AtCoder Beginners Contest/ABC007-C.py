# ABC007 - C

# マス目空間上で幅優先探索を行う問題
# 基本的には幅優先探索のひな型をベースに探索を行いつつ、その過程で各マスの距離情報を何かしらの形で記憶していくことで解が得られる

import copy
from collections import deque
H,W = map(int,input().split())
sy,sx = map(int,input().split())
gy,gx = map(int,input().split())
tmp_map = [list(input()) for i in range(H)]

def view_grid(field): # 現在のマス情報を出力
    for row in field:
        print("".join(row))
    print()
    return

Grid = copy.deepcopy(tmp_map)
# "s" : スタートマス, "g": ゴールマス
# "-" : 確認済みマス, "*": 訪問済みマス
Grid[sy-1][sx-1] = "s"
Grid[gy-1][gx-1] = "g"

ny,nx = sy-1,sx-1
dy = [-1, 0,+1, 0]
dx = [ 0,+1, 0,-1]

search_queue = deque()
search_queue.append([0,ny,nx]) # キューにスタート位置の距離情報とマス情報を追加

distances = [[] for i in range(H*W)]
distances[0] = [[ny,nx]]

while(len(search_queue) != 0):
    #print(search_queue)
    d,ny,nx = search_queue.popleft() # キューから確認済みマスの情報を受け取る
        
    if Grid[ny][nx] == "g": # 取り出したマスがゴールな終了
        #print("ended")
        distances[d+1].append([ny,nx])
        break
    
    Grid[ny][nx] = "*" 
    #view_grid(Grid)
    for k in range(len(dx)):
        y,x = ny+dy[k],nx+dx[k]
        if Grid[y][x] == "g": # 取り出したマスがゴールなら印をつけずにキューにマス情報を格納後そのまま周辺の探索を終了
            search_queue.append([d+1,y,x])
            distances[d+1].append([y,x])
            break
            
        if Grid[y][x] not in ["#","*","-"]: # 未探索マスなら確認済みマスの印をつけてキューに格納
            Grid[ny+dy[k]][nx+dx[k]] = "-" 
            search_queue.append([d+1,y,x])
            distances[d+1].append([y,x])

ad,ay,ax = d,ny,nx # 探索終了(ゴール発見)時点で取得していたマス情報を得る
print(ad) # 距離情報を取得