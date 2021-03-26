#AGC010 - A

n = int(input())
a = [int(x) for x in input().split()]
cnt_odd = 0
cnt_even = 0

# 奇数+奇数=偶数, 偶数+偶数=偶数なので、偶奇いずれに対して処理を行うにしても、偶数要素は常に用意することができる
# 奇数要素が奇数個ある場合、最後に奇数要素が一つ余りこれによって要素が1つだけにならない
# なお、制約は 2 <= N <= 100000なので N=1のときは考慮しなくてよい
# ここまで分かれば、コードの記述は難しくない

for ele in a: # 偶数要素をカウント
    if ele%2 == 0:
        cnt_even += 1

cnt_odd = n-cnt_even # 偶数要素以外が奇数要素

if cnt_odd%2 == 0: # 奇数要素が偶数個なら"YES"
    print("YES")
else:
    print("NO")