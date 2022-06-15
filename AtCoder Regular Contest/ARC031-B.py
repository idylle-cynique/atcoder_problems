# ARC031 - B

# グリッド(マス目)の全探索アルゴリズムの実装を求める問題
# 海であるマスをそれぞれ順番に取り上げて、そのマスを埋め立てて行ったときに陸地が全て一つにまとまるか調べ上げていき
# 陸地が全て一つにまとまるものが見つかったときはYES, 見つからないまま全探索を終えたときはNOと出力する
# ただグリッドの全探索をするだけなので、陸地が全て一つにまとまるか調べるのに用いる実装は
# 幅優先探索(BFS)、深さ優先探索(DFS)いずれを用いてもよい

# なお「陸地が全て一つにまとまるか」のチェックには、埋め立て後のグリッドを全探索によって逆に掘り起こして海にしていき、
# 陸地が消滅するかしないか……というやり方を用いている

from collections import deque
from copy import deepcopy 

Grid = []

def Grid_BFS(grid,x,y): # 初期位置から連続している陸地を全て海にする
    search_queue = deque() # 探索情報を格納するための両端キューを生成
    dy = [-1, 0,+1, 0]
    dx = [ 0,+1, 0,-1]
    
    for i in range(len(dx)): # 初期位置の周辺にある陸地(海化可能なマス)をチェック
        if grid[y+dy[i]][x+dx[i]] == "o": # 陸地が見つかった場合は探索用キューに格納
            search_queue.append([y+dy[i],x+dx[i]])

    #print(search_queue)
    while(len(search_queue) != 0): # 探索すべきマス(陸地)がなくなるまで探索
        #print(search_queue)
        ny,nx = search_queue.popleft() # 次の探索情報を受け取る
        grid[ny][nx] = "x"             # 得たインデックス位置の陸地を海にする
        for k in range(len(dx)): # 現在地周辺に陸地がないか調べ、あった場合は探索用キューに格納
            y,x = ny+dy[k],nx+dx[k]
            if grid[y][x] == "o":
                search_queue.append([y,x])
    return field

def check_ground(field): # 陸地がまだ存在しているかチェック
    h,w = len(field),len(field[0])
    for i in range(h):
        for j in range(w):
            if field[i][j] == "o": # 存在していた場合は False
                return False
    return True # 存在しなかった場合は True

def view_grid(field): # デバッグ用出力関数
    for row in field:
        print("".join(row))
    print()
    return

for i in range(12): # グリッド情報を受け取る
    if i == 0 or i == 11: # インデックスのオーバーフローを避けるための上端・下端のフレーム処理
        Grid.append(list("x"*12))
    else:
        Grid.append(list("x" + input() + "x"))
   
for j in range(1,len(Grid)-1): # 二重ループで順番にインデックスを得る
    for i in range(1,len(Grid[0])-1):
        if Grid[j][i] == "x":  # 対象の位置にあるのが海のマス"x"なら埋め立て処理をしてみる
            sy,sx = j,i # インデックスの受取
            
            field = deepcopy(Grid)          # 元のグリッド情報を破壊しないようdeepcopyでコピー
            field[sy][sx] = "x"
            #view_grid(field)
            
            field = Grid_BFS(field,sx,sy)   # BFSによる全探索で連続した陸地を海にし、そのグリッド情報を受け取る
            #view_grid(field)
            
            flag = check_ground(field)      # 受け取ったグリッドでは陸地が消滅していたか？
            
            if flag == True:                # 陸地が消滅していた場合は"YES"で終了
                print("YES")
                exit()

print("NO") # 条件を満たせるマスが見つからなかった時