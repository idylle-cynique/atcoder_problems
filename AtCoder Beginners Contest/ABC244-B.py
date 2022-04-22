# ABC244 - B

'''
    問題で要求されている処理をそのまま実装すればよい
    ここではある方向を向いている状態から前進処理をしたときの処理と、
    ある方向を向いている状態から90度回転処理をしたときの
    次に向くことになる方向に関する情報を連想配列で用意しておき、
    これらを参照することで繰り返し処理内の面倒な分岐処理などを省いて実装している
'''

N = int(input())
Commands = input()

nesw = "E"
move = [1,0]        # 進行方向の情報
coordinate = [0,0]  # 座標の情報
neswdict = {"N":"E", "E":"S", "S":"W", "W":"N"}
movedict = {"N":[0,1], "E":[1,0], "S":[0,-1], "W":[-1,0]}

for c in Commands:
    #print(c,":",coordinate,move)
    if c == "S":
        coordinate[0] += move[0]
        coordinate[1] += move[1]
    
    if c == "R":
        nesw = neswdict[nesw]
        move = movedict[nesw]

answer = " ".join([str(x) for x in coordinate])
print(answer)