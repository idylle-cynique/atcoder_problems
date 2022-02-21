# ABC233 - C

'''
    本番では面食らってしまい解答できなかったが、冷静に問題文を読んでみると
    ”袋に入っているボールの個数の総積は 10^5 を超えない。”とある。これは
    「全ての袋から1つずつボールを取り出すときの場合の数は最大でも10^5までしかない」
    さらに直接的に言い換えると「ボールの取り出し方について全探索が適用可能である」ということ

    ここまで分かれば、あとは実際に全探索を行うだけでいい
    入力値を得たあと、i番目の袋からi+1番目の各要素との積を記録していき、
    最後までやった後に残っている数のリストが
    「全ての袋から1つずボールを取り出したときの総積として考えられる全ての値」である
'''

N,X = map(int,input().split())
Lengths = []
Values = []

for i in range(N): # 入力値の受取
    tmp = [int(x) for x in input().split()]
    L,A = tmp[0],tmp[1:]
    Values.append(A)

Products = [1] # 考えられる積のリストを格納する
answer = 0

for i in range(N):
    tmp_values = []
    for pre_ele in Products: # i-1番目のリストまでで総積として考えられる全ての値を順番に取り出す
        for ele in Values[i]: # i番目の袋とi-1番目までで得られた積のリストとの積について、全パターン記録
            tmp_values.append(pre_ele * ele)
    Products = tmp_values # 得られた積でProductsリストを更新
    
#print(Products)

for ele in Products: # 数え上げ
    if ele == X:
        answer += 1
        
print(answer)
    