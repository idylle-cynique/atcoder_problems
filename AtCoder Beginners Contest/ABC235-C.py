''' ABC235 - C
    与えられる数列の長さ(要素数)はそれなりに多く、そのままクエリの処理をその都度
    線形探索などを利用して行うと計算量がO(N・Q)と大きくなってしまい処理が間に合わない
    また与えられた数列は各値の順番も意味を持つので、ソート処理などを事前に行うことなどもできない
    
    そのため、与えられた数列を直接いじるのではなく、別のデータ構造を用いて数列内の要素を整理しなおし
    高速にクエリを処理できるような形に変換する必要がある

    この問題では、連想配列(ハッシュテーブル)とリスト(配列)の組み合わせを用いて、各数値が数列中の何番目に存在するか
    上手く整理することで問題で求められている処理を時間の制約内で行うことができる
'''

N,Q = map(int,input().split())
A = [int(x) for x in input().split()]

NumsDict = {}   # 数列中に出現する要素の種類と、その要素を格納しているリストの添え字(ポインタがわり)を記録
NumsSet = set() # 線形探索中に出現した数値を記録
NumsData = [[] for _ in range(N*2)] #
#print(NumsData)

for i in range(N):
    ele = A[i]
    if ele not in NumsSet: # まだ記憶領域を確保していない数値のときは新規に割り当て
        NumsDict[ele] = len(NumsSet)+1      # 空いているリストの添え字を割り当て、それを辞書型で数値と対応付ける 
        NumsData[NumsDict[ele]].append(i+1) # 対応するリストの行にappend
        NumsSet.add(ele)                    # 割り当て済みの数値として記録
    else:                  # すでに割り当て済みならそのまま対応する二次元リストにappend()
        NumsData[NumsDict[ele]].append(i+1)

#print(NumsDict); print(NumsData)   

for i in range(Q):
    x,k = map(int,input().split()) # クエリの入力を受付
    #print(x,k,end=":")
    
    if x not in NumsSet:                  # 数列中に存在しない値のとき
        print(-1)
    elif len(NumsData[NumsDict[x]]) < k:  # 数列中のxでk番目の値が存在しないとき
        print(-1)
    else:                                 # 条件を満たすものが存在するとき
        checklist = NumsData[NumsDict[x]] 
        print(checklist[k-1])