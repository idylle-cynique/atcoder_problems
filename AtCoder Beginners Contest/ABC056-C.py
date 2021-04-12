# ABC056 - C

# 減算(x-i)処理を行うことなく入力値を作り出せることは明らか
# また1,2,3の3つで 1,2,3,4(1+3),5(2+3),6(1+2+3)と作っていけるように、Xまでの正整数値があれば 
# sum([int(n) for n in range(1,x+1)])までの正整数値を必ず用意することができる
# あとはこれに見合う累積和リストを事前に用意し、それに合わせて解を提示すればよい

# 累積和は昇順に整列されているので、複数の値が与えられる場合は線形探索ではなく二分探索を利用することで
# 高速に解を提示することができる

import itertools

x = int(input())

nums = [int(x) for x in range(1,10**5)]
nums_acmd = list(itertools.accumulate(nums)) # 累積和リスト

for i in range(len(nums_acmd)):
    #print(x,nums_acmd[i])
    if x <= nums_acmd[i]:
        print(i+1)
        exit()