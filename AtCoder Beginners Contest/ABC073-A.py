# ABC073 - C

# ある数字が紙に書かれた回数が奇数ならメモに数字が残り、偶数なら数字は残らない、と考えられる
# 各数値の出現回数をCoutner()を用いて記録し、各要素の出現回数の偶奇でカウントを行えばよい
# 要求の通りに実装しても解答は可能

from collections import Counter

n = int(input())
a = [int(input()) for x in range(n)]
a_data = Counter(a)

ans = 0
#print(a_data)

for k,v in a_data.items():
    #print(k,v)
    if v%2 != 0:
        ans += 1

print(ans)