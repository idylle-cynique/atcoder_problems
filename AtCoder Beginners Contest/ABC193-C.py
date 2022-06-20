''' ABC193 - C
    自分の手で条件を満たす値を探してみるとわかるが、問題の条件を満たす値はそれほど多くなく、
    数え上げを行っても十分処理が間に合う程度の個数(10^7)程度に収まる

    したがって、特段なにか工夫する必要はなく、単にNが制約上の最大値(10^10)である場合でforループ、
    whileループなどを用いて全探索し値を全て求めた後、実際の入力値の条件を満たすものを数え上げていけばよい
'''

n = int(input())
nums = set()
ans = 0

for i in range(2,10**5+1):
    j = 2
    while(i**j <= 10**10):
        #print(i**j)
        nums.add(i**j)
        j += 1

nums = sorted(nums)

for i in nums:
    if i <= n:
        ans += 1
    else:
        break

print(n-ans)
