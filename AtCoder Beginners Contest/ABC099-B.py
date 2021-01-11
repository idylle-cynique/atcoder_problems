# ABC099 - B
# 累積和を用いて解く問題
import itertools

a,b = [int(x) for x in input().split()]
temp = [int(x) for x in range(1,1000)]
nums = list(itertools.accumulate(temp))
nums_differ = [nums[i+1]-nums[i] for i in range(0,998)]

for i in range(len(nums_differ)):
      if nums_differ[i] == b-a:
            print(nums[i]-a)
            exit()