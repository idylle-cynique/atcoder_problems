# ABC211 - C

'''
動的計画法の利用を求める問題
行の長さ = |"chokudai"|, 列の長さ = |入力文字列Sの長さ| である二次元のDPテーブルを用意し
入力文字列Sの最初からi番目までの文字列を使って、文字列"chokudai"のj文字目までを選択したとき有り得る組み合わせの数
を左上から順に計算していくことで、問題で要求されている部分を最後に導出することができる
これによって、単純な全探索を用いた場合の計算量(O(N^8))に対してO(N)と断然高速に探索を行うことができる
'''

S = input()
C = len("chokudai")
chokudai = "chokudai"
MOD = 10**9+7

dp = [[0]*(len(S)+1) for _ in range(C+1)]

def view_dp(DP): # DPテーブルの閲覧
    for r in DP:
        print(r)
    print()
    return True
    
for j in range(len(S)+1):
    dp[0][j] = 1
    
#view_dp(dp)
for j in range(1,len(S)+1):
    for i in range(1,C+1):
        #print(S,"の{:3}文字目の{:}までを使って、chokudaiの{:}番目の{:8}を選ぶ場合の組み合わせの数".format(j,chokudai[i-1],i,chokudai[:i])); print(i,j,S[j-1],chokudai[i-1])
        if S[j-1] != chokudai[i-1]: # S[j]が使えない場合
            '''
            Sのj-1文字目まで使って,chokudaiのi番目までの文字列を作ったときの候補数と同じ
            すなわち、 dp[i][j-1] の値がこの時の候補数
            '''
            dp[i][j] = dp[i][j-1]
        else:                       # S[j]が使える場合
            '''
            S[j]を使った場合の候補数 + S[j]を使わない場合の候補数がこの時の候補数となる
            
                (1) S[j]を使った場合
                chokudaiのi番目に使う文字位置をSのj番目に固定して、手前までの文字列(chokudaiのi-1番目まで)をS[j-1]番目から選ぶ
                ということなので、この時の候補数はそれまでに記録したdp[i-1][j-1]の値にあたる
                
                (2) S[j]を使わない場合
                Sのj-1番目まで使って, chokudaiのi番目までの文字列を作ったときの候補数、
                すなわち、 dp[i][j-1] の値がこの時の候補数となる
            
            したがって (1)+(2)は以下の計算式で求められる
            '''
            dp[i][j] = dp[i][j-1] + dp[i-1][j-1]

#view_dp(dp)
print((dp[-1][-1])%MOD) # 10**9+7の余りを取ったものが解になる