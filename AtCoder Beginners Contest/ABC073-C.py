# ABC073 - C
# pythonの場合集合型(set型)が存在するので非常に話が早い

n = int(input())
nums = set()
for i in range(n):
    memo = int(input())
      
    if memo not in nums:
        nums.add(memo)
    else:
        nums.discard(memo)

print(len(nums))