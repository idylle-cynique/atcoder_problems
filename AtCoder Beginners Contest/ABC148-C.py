# ABC148 - C

# 問題を端的に言い換えると「与えられた二数の最小公倍数を求めよ」となる
# あとはそのまま実装するだけ

import math

a,b = [int(x) for x in input().split()]
lcm = (a*b) // math.gcd(a,b)

print(lcm)