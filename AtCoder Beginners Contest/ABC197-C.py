# ABC197 - C

# XOR,OR演算とbit全探索アルゴリズムの実装を要する問題
# 本番では、最大n-1個の区間にまで分けるのではなく、2つの区間にさえ分ければよいと勘違いしてしまっていた

# 実装については、手間はかかるものの行き詰ってしまうようなものではなかった
# Python3.8.2での実行ではTLEになるが、実行時コンパイルのあるPyPy3で提出するとAC判定を貰える

def calc_OR(lst):  # 区間リストにおけるOR値を求める
    w = len(lst)
    ret = lst[0]
    for i in range(1,w):
        #print(ret,lst[i],":",ret|lst[i])
        ret = (ret|lst[i])
    return ret

def calc_XOR(lst): # OR値リスト内の値のXOR値を求める
    w = len(lst)
    ret = lst[0]
    
    for i in range(1,w):
        ret = (ret^lst[i])
    return ret
    
n = int(input())
a = [int(x) for x in input().split()]
ans = 2**30+1

if n == 1:
    print(min(ans,a[0]))
    exit()

for i in range(1,2**(n-1)): 
    idxs = [0]     # 区間インデックスリスト
    sects = []     # 区間リストのリスト
    OR_values = [] # 区間内OR値リスト
    
    for j in range(n-1): # bit探索で分割する区間インデックスリストを作成
        #print(j,":",(i>>j)&1)
        if (i>>j)&1 == 1:
            idxs.append(j+1)
    idxs.append(n)
    
    for i in range(len(idxs)-1): # 区間インデックスリストを使ってリストaを実際に分割
        sects.append(a[idxs[i]:idxs[i+1]])
    #print("".join([str(sects[i]) for i in range(len(sects))])) # 中身の確認
    
    for i in range(len(sects)):  # 区間リストのリストからそれぞれのOR値を求める
        OR_values.append(calc_OR(sects[i]))
    #print(OR_values)
    
    ans = min(ans,calc_XOR(OR_values))

print(ans)