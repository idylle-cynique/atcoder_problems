# ARC059 - C

# どのようにすればコストの最小化を図れるのかについてざっくり考えてみると
# 数列Aの要素のうちmin(A) <= x <= max(A)を満たす値xのうちのどれかであると推測できる
# ただ、実際の数列中の値の偏り方によってxとするべき値は変わるので、
# そのうちのどれなのかを一発で求めたりはせず、制約が -100 <= A_i <= 100であることに着目して
# 全探索で解を求めることにする

# N = 100, -100 <= A_i <= 100より、200*100 = 20000回程度のループで処理を終えることができるので
# 十分高速に処理が可能

N = int(input())
A = [int(x) for x in input().split()]

min_ele = 100
max_ele = -100

for ele in A: # 数列中の最小の値、最大の値を求める
    min_ele = min(ele,min_ele)
    max_ele = max(ele,max_ele)

#print(min_ele,max_ele)
ans = float('INF')

for x in range(min_ele,max_ele+1): # min(A) <= X <= max(A)の範囲で全探索
    tmp = 0
    for ele in A:
        tmp += ((ele-x)**2)
    #print(ans,":",tmp)
    ans = min(ans,tmp)

print(ans)