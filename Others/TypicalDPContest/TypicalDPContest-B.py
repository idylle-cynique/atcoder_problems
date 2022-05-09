# TDPC - B

# a,b = map(int,input().split())
# A = [int(x) for x in input().split()]
# B = [int(y) for y in input().split()]

a,b = 5,5; A = [2, 4, 5, 4, 2,]; B = [2, 8, 3, 4, 5,]
dp = [[0 for i in range(a+1)] for j in range(b+1)]

for row in dp: print(row)

# 左の山にi個、右の山にj個あるときのSnuke君の最適解を求めていく

for i in range(a,-1,-1):
    for j in range(b,-1,-1):
        print(i,j)

        if i == 0 and j == 0: # 左右の山のいずれも空ならゲーム終了
            break
        elif i == 0: # 左の山が空の時は、右の山から取る
            pass
        elif j == 0: # 右の山が空の時は、左の山から取る
            pass
        else:        # 左右いずれからも取ることができるなら、より価値の高い方を取る
            pass



    else:
        break
