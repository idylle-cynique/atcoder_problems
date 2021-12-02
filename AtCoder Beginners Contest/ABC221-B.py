# ABC221 - B

'''
S,Tの文字列の長さが2～100と短く、かつ入れ替え処理を行うのは一回(ないしゼロ)きりなので
そのまま入れ替え処理を行って得られる文字列のパターンを全て試せばよい
'''

import copy

S = list(input())
T = list(input())

U = copy.deepcopy(S)
V = copy.deepcopy(T)
flag = False # 使わなかった

if U == V: # そもそもswap処理が必要ない(0回のswapで同じになる)場合
    print("Yes")
    exit()

for i in range(1,len(S)):
    if U[i] != T[i]:
        if i == 0:          # リストの先頭のとき
            U[i],U[i+1] = U[i+1],U[i]
            if U == V:
                print("Yes")
                exit()
        elif i == len(S)-1: # リストの末尾のとき
            U[i-1],U[i] = U[i],U[i-1]
            if U == V:
                print("Yes")
                exit()
        else:                # それ以外のとき
            U[i],U[i+1] = U[i+1],U[i] # 右隣の文字とswap
            if U == V:
                print("Yes")
                exit()
                
            U[i-1],U[i] = U[i],U[i-1] # 左隣の文字とswap
            if U == V:
                print("Yes")
                exit()

print("No") # "Yes"の出力を経ずに全探索を終えた場合"No"