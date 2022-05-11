''' ABC250 - A
    問題で要求されている通りの処理をそのまま実装するだけでよいが
    H,W = 1,1, H,W = 1,2 H,W = 2,1 のような入力例もあることを
    考慮に入れながら場合分けを適切に行うこと
'''
H,W = map(int,input().split())
R,C = map(int,input().split())

if H == 1 and W == 1: # 1マスしかないとき
    print(0)
elif H == 1:          # 1行しかないとき
    if C in (1,W):
        print(1)
    else:
        print(2)
elif W == 1:          # 1列しかないとき
    if R in (1,H):
        print(1)
    else:
        print(2)
else:                 # 行、列いずれも2以上あるとき
    if (R,C) in ((1,1), (1,W), (H,1), (H,W)):
        print(2)
    elif R in (1,H) or C in (1,W):
        print(3)
    else:
        print(4)