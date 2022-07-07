''' ABC235 - B
    要求された処理をそのまま実装するだけでよい
    ただし、早とちりしてmax関数などを用いたりしないこと
'''

N = int(input())
H = [int(x) for x in input().split()]
pre = 0

for now in H: # 台を順番に見ていく
    #print(pre,now)
    if pre < now: # 次の台が今いる台より高いなら移動
        pre = now
    else:         # そうでないなら移動終了
        break

print(pre)