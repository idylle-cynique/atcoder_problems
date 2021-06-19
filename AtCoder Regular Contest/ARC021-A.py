# ARC021 - A

# あるマスとその上下左右のいずれかの隣り合うマスとの値が同じあるマスが存在していればCONTINUE
# 9つのマスのどこにも存在しなければGAMEOVERとなる
# あとはインデックスの範囲外参照にだけ注意しながら、上記の実装を行えばよい

NumTile = [[int(x) for x in input().split()] for y in range(4)]

for j in range(0,4):
    for i in range(0,4):
        #print(NumTile[j][i],NumTile[j+1][i]); print(NumTile[j][i],NumTile[j][i+1])

        if i<3: # 右端のマス以外のときだけ右隣のマスを参照
            if NumTile[j][i] == NumTile[j][i+1]: # 横に隣り合うマスの値は等しい？
                print("CONTINUE")
                exit()
        
        if j<3: # 下端のマス以外のときだけ下のマスを参照
            if NumTile[j][i] == NumTile[j+1][i]: # 縦に隣り合うマスの値は等しい？
                print("CONTINUE")
                exit()

print("GAMEOVER") # 条件を満たすマスが見つからないまま探索を終えてしまったとき