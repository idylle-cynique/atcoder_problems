# AGC007 - A

# 問題の内容を言い換えると、条件を満たすような駒の動かし方をしたとき、
# 入力値に示したルートをそのまま全てなぞることが出来たか、ということ
# したがって、実際に右ないし下への移動を行ってその軌跡"*"を作り、"#"をそのまま塗りつぶせたかどうか調べればよい

H,W = map(int,input().split())

Grid = []

def view_grid(field): # グリッド情報を確認
    for row in field:
        print("".join(row))
    return

for i in range(H+2): # グリッド情報を受取
    if i == 0 or i == H+1:
        Grid.append(list("x"*(W+2)))
    else:
        Grid.append(list("x" + input() + "x"))

ny,nx = 1,1

while(ny != H+1 and nx != W+1): # 右下の端にたどり着くまで探索
    Grid[ny][nx] = "*"
    
    if Grid[ny+1][nx] == "#":
        ny = ny+1
    elif Grid[ny][nx+1] == "#":
        nx = nx+1
    else:
        break
    #view_grid(Grid)
#view_grid(Grid)

for j in range(1,H+1): # 軌跡を生成していったとき、全ての"#"が塗りつぶされたか確認
    for i in range(1,W+1):
        if Grid[j][i] == "#": # 塗りつぶされていない部分が見つかった場合は Impossible
            print("Impossible")
            exit()

print("Possible") # 塗りつぶされていない部分がなかった場合は Possible
    
    