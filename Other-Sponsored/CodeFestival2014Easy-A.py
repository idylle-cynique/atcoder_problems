# Code Festival 2014 Easy - A

# 要求されたとおりに実装すればよい
# これは偶然気づいたことだが差の合計値をインクリメントによって記録していくより
# 各差の値をリストに格納していき、最後にsum()を用いてその合計を求めた方が計算速度がより速い
# 確認できるように関数の形で示しておいたので、試したい場合は利用すること
# 理由は不明だが、以後はひとつ頭に置いておきたい

N = int(input())
A = [int(x) for x in input().split()]
sum_diffs = 0

def another_answer():
    A_diffs = []
    for i in range(N-1):
        A_diffs.append(A[i+1]-A[i])
    print(sum(A_diffs)/(N-1))
    return 

#another_answer() # コメントアウトを外せば利用できる

for i in range(N-1):
    sum_diffs += A[i+1]-A[i]

print(sum_diffs/(N-1))