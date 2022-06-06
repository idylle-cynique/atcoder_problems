# AGC033 - A

# 幅優先探索(BFS)アルゴリズムへの理解と実装を求める問題 
# 基本的には各黒マスを探索キューに入れて上下左右を黒くしていくとともに、
# それが元あった黒マスから何マス離れた位置にあるマスなのかを距離情報を格納するマップに記録していき
# そのうちの最大値を出力していけばよい

# ただし、実際の実装で求められているような黒塗り処理をそのまま実装するとPython3ではTLEになるので
# グリッド情報は探索にだけ利用し、生成するマップは黒塗り処理を施したマップが元の黒マス(最も近い黒マス)
# からいくつ離れているかを記録するマップだけにすること

# また、古い問題ゆえ制限実行時間が1000msとシビアでPython3ではTLEとなって通らず、PyPy3でないと通らない

from collections import deque
from copy import deepcopy
 
H,W = map(int,input().split())
Grid = []
DistMap = [[-1 for i in range(W+2)] for j in range(H+2)] 
dy = [-1, 0,+1, 0]
dx = [ 0,+1, 0,-1]
 
for i in range(H+2): # グリッド情報を受取
    if i == 0 or i == H+1:
        Grid.append(list("x"*(W+2)))
    else:
        Grid.append(list("x" + input() + "x"))

for j in range(H+2):
    for i in range(W+2):
        if j == 0 or j == H+1: # フレームマスには適当に大きな値を入れておく
            DistMap[j][i] = H*W
            continue
        
        if i == 0 or i == W+1: # フレームマスには適当に大きな値を入れておく
            DistMap[j][i] = H*W
            continue
        
        if Grid[j][i] == "#":  # 黒マスが始点になるので、距離は0としておく
            DistMap[j][i] = 0

def view_grid(field): # グリッド情報を確認
    for row in field:
        print("".join(row))
    return True
 
def view_distmap(distmap):
    for row in distmap:
        print(row)
    return True
 
def Grid_BFS(field):
    search_queue = deque()
    d = 0
    
    for j in range(1,H+1): # 探索用の黒マスを探していき、探索キューに格納
        for i in range(1,W+1):
            if DistMap[j][i] == 0: 
                search_queue.append([j,i,d]) # y座標: j, x座標: i, 距離情報: d
    

    while(len(search_queue) != 0):
        #view_grid(field)
        ny,nx,nd = search_queue.popleft() # 探索キューから要素を取り出す
        nd += 1
        for k in range(len(dx)): # 上下左右のマスを探索
            y,x = ny+dy[k],nx+dx[k]
            if DistMap[y][x] == -1: # 未訪問のマスなら情報を更新
                search_queue.append([y,x,nd]) # 距離情報に1を加えて探索キューにエンキュー
                DistMap[y][x] = nd            # 距離情報マップに距離情報を記録
                #field[y][x] = "#"

    return nd-1 # 最後に保持していた距離情報から-1したものを戻り値とする

print(Grid_BFS(Grid))
#view_distmap(DistMap)

