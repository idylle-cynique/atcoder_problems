# ABC199 - C

# 試験中にAC判定を得ることができたが、解説で示される解法と異なるので、解説も参照するとよい
# https://atcoder.jp/contests/abc199/editorial/1162

# クエリにおける T=2 の処理をそのまま問題文の通りに実装すると、要素のずらし処理に都度O(N)の処理が必要となってしまう
# このままQ回のループ処理を行うと O(N*Q) の計算量となり、到底2000msでは処理が間に合わない

# そこで、処理対象であるSを右半分と左半分に分割した上で
# T=1の処理は、クエリで受け取ったインデックスの値を調整したうえでそのままswap処理する
# T=2の処理は、左半分の文字列を格納したリストと右半分の文字列を格納したリストをswap処理する
# というふうにする。この場合リスト2つのswapは直接値を書き換えるのではなく、単に相互にオブジェクトidを入れ替えるだけなので、
# 通常処理時のようにO(N)の処理が発生することがない
# この特性を確認出来るようにswap_id関数を示したので必要な場合は確認に用いること

def swap_id(lst_a = [1,2,3],lst_b = [2,4,6]):
    # swapする前の各リスト変数のID
    print("a_id:",id(lst_a)) ;print("b_id:",id(lst_b))

    lst_a, lst_b = lst_b,lst_a # swap処理

    # swapした後の各リスト変数のID
    print("a_id:",id(lst_a)); print("b_id:",id(lst_b))
    return

N = int(input())
S = list(input())
Q = int(input())

left_string = S[:N]  # Sの左半分
right_string = S[N:] # Sの右半分

for query in range(Q):
    T,A_idx,B_idx = map(int,input().split())
    #print(left_string,right_string); print(T,A_idx,B_idx)
    if T == 1: 
        if A_idx<=N and B_idx<=N:   # いずれのインデックスも左半分にあるときの添え字処理
            A_idx -= 1 
            B_idx -= 1
            left_string[A_idx],left_string[B_idx] = left_string[B_idx],left_string[A_idx]
        elif A_idx<=N and B_idx>N:  # 片方のインデックスが左半分、もう片方が右半分にあるときの添え字処理
            A_idx -= 1
            B_idx -= (N+1)
            left_string[A_idx],right_string[B_idx] = right_string[B_idx],left_string[A_idx]
        else:                       # いずれのインデックスも右半分にあるときの添え字処理
            A_idx -= (N+1)
            B_idx -= (N+1)
            right_string[A_idx],right_string[B_idx] = right_string[B_idx],right_string[A_idx]
        
    if T == 2:      # T=2 のときはオブジェクトidの交換によるswap
        left_string,right_string = right_string,left_string

cat_string = left_string + right_string # 分割していた文字列を元に戻す

print("".join(cat_string)) # join()を用いて出力