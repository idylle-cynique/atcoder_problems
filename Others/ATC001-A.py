# AtCoder Typical Contest 001 - A: 深さ優先探索
# AtCoder公式による典型問題集

# ひとまずトップの解説を見ながら実装したもの
# コードについては自分で考えたものだが、結果的にはスタック(未通過マスのリストへの追加・末尾取り出し)による実装
# ほぼそのままという感じになった。再帰関数による実装の方が再利用しやすいので、別途コードを書いておきたい

H,W = map(int,input().split())
grid = []

def view_grid(field): # 現在の迷路の探索状況を出力
    print()
    for row in field:
        print("".join(row))
    return

for i in range(H+2):  # 外部参照防止のためのフレーム処理
    if (i==0) or (i==H+1):
        grid.append(["#"]*(W+2))
    else:
        grid.append(["#"] + list(input()) + ["#"])

dx = [ 0,+1, 0,-1]
dy = [-1, 0,+1, 0]
i,j = 1,1 # 現在の位置のインデックスを記憶
yet = []  # まだチェックしていない道の位置リスト
f = False

for y in range(1,H+1): # スタート地点の位置を探索
    for x in range(1,W+1):
        if grid[y][x] == "s":
            f = True
            i,j = y,x
            break
    if f == True:
        break

while(grid[i][j] != "g"):
    #view_grid(grid); print(yet)
    grid[i][j] = "*"
    
    for k in range(len(dx)):  # 現在の位置の周辺の情報を調べる
        y,x = i+dy[k],j+dx[k]
        
        if grid[y][x] == "g": # ゴールが見つかったら終了
            print("Yes")
            exit()
            
        if grid[y][x] == ".": # 通れる道を発見したらまだ通っていない道リストに位置情報を格納
            yet.append([y,x])

    if len(yet) == 0: # 通れる道がもうない場合は到達不可能と判断
        print("No")
        exit()
    else:             # まだ通れる道があるならリストの最後尾を取り出してそこから調べなおす
        i,j = yet.pop()