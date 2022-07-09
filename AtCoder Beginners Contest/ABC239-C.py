# ABC239 - C

'''
    問題中で示されている図と制約を見てみると自ずと見当がつくが、
    整数値で示された座標からのユークリッド距離が√5であるx,yともに整数値であるような座標は
    元の座標をX,Yとした場合
    (X+1,Y+2), (X+1,Y-2), (X-1,Y+2), (X-1,Y-2), (X+2,Y+1), (X+2,Y-1), (X-2,Y+1), (X-2,Y-1)
    にあたる8つの座標しかない。

    ということは、入力されたふたつの座標において、上8つに相当する座標群を求め、
    その中に共通の座標が含まれるかどうかを調べればよい
'''

X1,Y1, X2,Y2 = map(int,input().split())
points = [-2,-1,+1,+2] # 逐一列挙するとタイプミスによる誤動作が有り得るので、ここではループ処理を利用している
coodinates1 = []
coodinates2 = []

for n in points:
    for m in points:
        if abs(n) == abs(m): #二値の組み合わせのうち絶対値がことなる組み合わせのみ試す
            continue
        #print(n,m)
        coodinates1.append((X1+n,Y1+m))
        coodinates2.append((X2+n,Y2+m))

for a in coodinates1:   # 座標群の組み合わせを全列挙して、共通の座標の組み合わせが見つかるか調べる
    for b in coodinates2:
        x1,y1 = a
        x2,y2 = b
        
        if x1 == x2 and y1 == y2: # 見つかったらYesを出力して終了
            print("Yes")
            exit()

print("No") # 見つからなかったらNoを出力して終了