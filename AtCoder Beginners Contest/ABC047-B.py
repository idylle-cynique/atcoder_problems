'''ABC047 - B
    問題文で求められている処理をそのまま実装すればよい問題
    処理の実現方法にはいくつか種類があるが、ここでは色の塗られていない四角形領域のうち
    上底のy値, 下底のy値, 左端のx値, 右端のx値を更新していき、それらの情報を用いて最後に面積を計算する
    という具合に処理している
    この方針では、入力値によって上底と下底の値・左端と右端の値の大小が逆転する(各端からの重ね塗りが発生する)
    場合があるので、面積の算出時にコーナーケースとして別途処理する必要があるので注意したい
'''
W,H,N = map(int,input().split())
top,bottom = H,0
left,right = 0,W

for i in range(N):
    x,y,a = map(int,input().split())
    
    if a == 1:      # a=1 のときは長方形の x<xi をみたす領域
        left = max(left,x)
    elif a == 2:    # a=2 のときは長方形の x>xi をみたす領域
        right = min(right,x)
    elif a == 3:    # a=3 のときは長方形の y<yi をみたす領域
        bottom = max(bottom,y)
    else:           # a=4 のときは長方形の y>yi をみたす領域
        top = min(top,y)
        
#print(top,bottom,right,left)
if (top-bottom) < 0 or (right-left) < 0: # 高さや幅の情報に負数が含まれているときは、全領域に色が塗られたとき
    print(0)
else:
    area = (top-bottom)*(right-left)
    print(area)