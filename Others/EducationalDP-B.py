# Educational DP Contest - B

'''
A問題を拡張したもの
1～100個までの任意の数まで飛ばして足場を移動することができる、というふうになっているが、解き方としてはA問題とそれほど変わりはない
ここでの用意するDPテーブルは一次リストで、 dp[i] = 足場iへ 足場i-j(1<=j<=k)から移動するときの最小移動コスト
というふうに定義して考えることで、リスト末尾に全体での最小移動コストが求められる
'''

N,K = map(int,input().split())
Scaffoldings = [int(x) for x in input().split()]

dp = [float("inf") for _ in range(N)] 
dp[0] = 0 # 足場0(スタート地点)までのコストは0
#print(dp)

for i in range(N):
    for j in range(1,K+1):
        if i-j >= 0: # 範囲外のインデックスへの参照を避ける
            #print("足場{}へ足場{}-{}={}から行った時の最小コストを更新する".format(i,i,j,i-j))
            dp[i] = min(dp[i-j]+abs(Scaffoldings[i]-Scaffoldings[i-j]), dp[i])

            '''
            (1) j個前の足場に行くまでの最小コスト(dp[i-j]) + j個前からi番目の足場に移動した時のコスト
            (2) それまでに分かっているi番目の足場に行くまでの最小コスト
            のいずれかのうち、小さい方がその時点における最小移動コストとなる
            '''

print(dp[-1])