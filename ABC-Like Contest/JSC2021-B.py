# JSC2021 - B

# A集合とB集合からXOR処理を施した集合を抜き出せ、という問題。
# 集合演算にあたってはそのままXOR演算記号を使うこともできるが、ここではOR集合とAND集合の差を求める形でXOR演算を行っている

N,M = map(int,input().split())
A_set = set([int(x) for x in input().split()])
B_set = set([int(x) for x in input().split()])
answer = (A_set|B_set) - (A_set&B_set)

if len(answer) == 0:
    print()
else:
    print(" ".join([str(i) for i in list(answer)]))