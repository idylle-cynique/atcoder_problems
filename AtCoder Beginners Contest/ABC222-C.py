''' ABC222 - C 
    問題文で要求されている処理をそのまま実装すればよい

    制約を見てみると、プレイヤー数は最大で100人、じゃんけん回数も最大で100回まで
    とあるのでじゃんけん処理の回数は高々100//2 * 100 = 5000回程度
    したがって、計算量を気にする必要性は全くない
    
    問題の処理の実装にあたっては、
    playerリストに勝利スコアとプレイヤー番号(添え字)を整数値として保持させ
    それらをi回戦目のじゃんけんの終了後ソートし、順位を再調整させている
    なお、ここでは順位調整処理をそのまま昇順ソートのみで実現されるように
    勝利スコアを負数で管理させている
'''


N,M = map(int,input().split())
players = [[0,int(n)] for n in range(N*2)] # (勝利数, プレイヤー番号)
jankens = [list(input()) for i in range(N*2)]

def judge_janken(a,b): # じゃんけんの判定
    if (a == b):                                     # 引分けパターン
        return -1
    elif (a,b) in (("G","C"), ("C","P"), ("P","G")): # aの勝ちパターン
        return 1
    else:                                            # aの負けパターン
        return 0


for i in range(M): # i回戦を行う
    for j in range(0,len(players),2):
        # j位のプレイヤーとj+1位のプレイヤーとでじゃんけん勝負を行う
        p1idx = players[j][1]
        p2idx = players[j+1][1]
        p1 = jankens[p1idx][i]
        p2 = jankens[p2idx][i]
        result = judge_janken(p1,p2)
        if result == 1:
            players[j][0] -= 1
        elif result == 0:
            players[j+1][0] -= 1
        else:
            pass
    players.sort()
    #print(f"{i+1}",players)

answer = [p[1]+1 for p in players]

for ans in answer:
    print(ans)