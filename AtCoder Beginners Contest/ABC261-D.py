''' ABC261 - D
    動的計画法の実装を求める問題
    問題における解(コインの最大獲得枚数)の導出過程そのものを直接的に求めることは難しいが
    個別のシチュエーションに至るまでの事前状態、すなわち
        「ある回数(x回目)でのコイントスでカウンタがyであるような状態に遷移可能な事前状態」
    に関しては、「x-1回目のコイントスでカウンタがy-1回目であるような状態」であるとすぐにわかる

    最適解そのものの導出過程を直接求めることは出来ないが、X-1回目までの最適解を元にX回目の最適解を求める
    という作業を積み重ねていって全体での最適解を求めることは可能らしいことがわかる
    ここまで分かれば解法は動的計画法がお誂え向きだ、ということが分かるので、
        「i回目のコイントスでカウンタがjであるときのコインの最大獲得可能枚数」
    を格納可能なDPテーブルを用意し、それを用いて各状態における最適解をi=1から順に求めておけばよい

    具体的な各状態における最適解は以下の通り
        i)   i < j (トス回数よりもカウンタの値の方が大きい) であるとき
            こうした状態に遷移することは出来ない (最適解が存在しない)
        ii)  j > 0 (カウンタが0より大きい) であるとき
            i-1回目のコイントスでカウンタがj-1であるときの最適解
             + コインが表の時の獲得コイン枚数 + ボーナスコイン枚数
        iii) j = 0 (カウンタが0に等しい) であるとき
            i-1回目のコイントスで遷移可能な一連の状態のうちの最適解(最も獲得可能コイン枚数が大きい状態)
    
    DPテーブルの大きさ分だけの計算が発生するので、計算量はO(N^2)
    Nの制約は最大5000なので 2.5 * 10^7 ほどのループ処理が発生することになるが、
    これはPython(PyPy)にとっては、場合によって実行制限時間を超過しかねないループ回数になるので
    解説で示されているような遷移不可能な状態に対して丁寧に -inf を与えていくような処理や
    遷移不可能な状態でもbreakせずに愚直にループさせるような処理を行わせるなどのやり方は避け
    省ける処理は省くようにする必要がある
'''

N,M = map(int,input().split())
reward = [int(x) for x in input().split()]
bonusdict = dict()
for _ in range(M):
    key,val = map(int,input().split())
    bonusdict[key] = val

dp = [[0 for i in range(N+1)] for j in range(N+1)]
pre_max = int(0)
bonus = int(0)
answer = int(0)

for i in range(1,N+1):
    for j in range(N+1):
        #print(f"{i}回目でカウンタが{j}の時に得られるコインの数の最大値を考える")
        if i < j:
            pass
        elif j: # カウンタが0以外のとき
            bonus = bonusdict[j] if j in bonusdict else 0
            dp[i][j] = dp[i-1][j-1] + reward[i-1]  + bonus
            pre_max = max(pre_max,dp[i][j])
        else: # カウンタが0のとき
            dp[i][j] = pre_max

#for row in dp: print(row)
answer = pre_max

print(answer)
