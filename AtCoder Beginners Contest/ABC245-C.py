'''ABC245 - C
    直接的に条件を満たす数列の生成可否を調べるのではなく、
    「数列A,Bのうちから1番目の要素からj番目の要素までを用いて条件を満たす数列を生成することは可能か」
    を小さい方から順番に探索しその可否を確定していき、
    最後にN番目の要素(全ての要素)までを使ったときの可否を調べ切れば自ずと解がわかる、ということになる

    早い話、動的計画法のアルゴリズムを利用して解きなさい、ということになる
    Nの制約が2*10^5と大きいが、探索はA,Bの2つの数列を
        i)   j列目のAの要素とその前の列のAの要素の絶対差
        ii)  j列目のAの要素とその前の列のBの要素の絶対差
        iii) j列目のBの要素とその前の列のAの要素の絶対差
        iv)  j列目のBの要素とその前の列のBの要素の絶対差
    を調べていく処理をN個全ての要素に対して行い、DPテーブルを生成していくだけなので
    全体での計算量はO(N)で済み、確かに制限時間内に処理を完了することができる
'''


N,K = map(int,input().split())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
rowspan = 2 # AとBの2種の数列のいずれかから選ぶので長さは2

dp = [[False for x in range(N)] for y in range(rowspan)]
AB = [A,B]

def printdp(lst): # dpテーブルの確認
    for row in lst: print(row)
    return

for i in range(2): # 1番目から1番目まで(つまり1番目だけ)の要素を使って条件を満たす数列を作ることは常に可能
    dp[i][0] = True

'''
    1番目(インデックス0)からi番目までの要素を使って数列を作り、
    j番目にA_iないしB_iを選んだ時に条件を満たす数列になるか
    を小さい方から順番に考えていく
'''

for j in range(1,N):
    for i in range(rowspan):
        temp = abs(dp[i][j-1] - dp[i][j])
        for k in range(rowspan):
            #print(AB[i][j-1],AB[k][j],"=",abs(AB[i][j-1] - AB[k][j]),K)
            if abs(AB[i][j-1] - AB[k][j]) <= K and dp[i][j-1]:
                dp[k][j] = True
        #printdp(dp)

answer = "No"

for i in range(rowspan): 
    if dp[i][N-1]:  # 完成したdpテーブルの最後列の要素にTrueが含まれるなら可能、ということ
        answer = "Yes"
        break

print(answer)