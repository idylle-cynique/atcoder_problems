''' ABC252 - D
    数列中から条件を満たす要素3つの組み合わせの数を求める問題
    そのまま3つの要素の組み合わせを全探索で列挙した場合、O(N^3)となりTLE
    2つ目まで全列挙して3つ目となり得るような要素の個数を二分探索などで一括して求める場合でも
    O(N^2・logN)となりやはりTLEとなる

    この問題を解く際に一番重要なのは、条件にあるA_i,A_j,A_kにおける
        「i < j < k」
    という条件はとくに考慮する必要はないということ
    何故かというと3つの要素の組を取り挙げるときにそれらが重複のない取り挙げられ方であれば、
    (3番目の要素, 5番目の要素, 2番目の要素)のような取り上げ方でもi=2, j=3, k=5というふうに読み替えが可能で、
    取り出した時点での並びを考慮する必要はないため

    すると、結局この問題は
        「A_i < A_j < A_kであるような数列中の要素3つの組み合わせの個数を求めよ」
    という形まで簡単化される

    その上で改めて問題を考えてみると条件を満たす組み合わせの取り挙げ方もかなり単純化できることがわかる
    3要素の値がそれぞれ異なりさえすればよいということは、
    A_j(2番目に大きい要素)を固定すれば、残りのA_iの選び方はA_j未満である要素、A_kはA_jより大きい要素から選べばよい
    ということ

    つまり事前処理で各値を取る要素の個数情報を配列や辞書などで用意しておき、
    jを一番小さい要素から順番にループで取り挙げ
    A_jを2番目の要素として選んだ時の組み合わせを
    「A_iとして選ぶことのできる要素(A_jより小さい要素)の個数 * A_jであるような要素の個数 * A_kとして選ぶことのできる要素(A_jより大きい要素)の個数」
    として一括して計算することができ、これらの組あわせ数の総和が解となる

    事前に行る各値を取る要素の個数の数え上げ処理にO(N)
    A_jを固定したときのA_i,A_j,A_kの選び方の数を求める処理にO(N)
    したがって全体の処理もO(N)で完遂することができる
'''
N = int(input())
Numbers = sorted([int(x) for x in input().split()])
counter = [0 for x in range(max(Numbers)+1)]

for n in Numbers:
    counter[n] += 1

prev_numbers = 0
next_numbers = N

answer = 0
for i,j in enumerate(counter):
    if counter[i]:
        next_numbers -= counter[i]
        #print(i,counter[i]); print(":",prev_numbers,counter[i],next_numbers,"->",prev_numbers * counter[i] * next_numbers)
        answer += (prev_numbers * counter[i] * next_numbers)
        prev_numbers += counter[i]

print(answer)