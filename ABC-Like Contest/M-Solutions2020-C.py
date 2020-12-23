# M-Solutions プロコンオープン2020 - C
nums = [int(x) for x in input().split()]
k = int(input())

# R < G < B の関係性が成り立つようにする。
# 一度の操作で任意のカードの数字を二倍にできる　⇒  数字の操作はnums[x] }* (2**n)ということ。
# k回の2倍化処理が可能で、カードの種類は3種類なので、 3**k通りのパターンが考えられる。

def nums_check(nums):
      if nums[0] < nums[1] and nums[1] < nums[2]:
            return True
      else:
            return False

for i in range(k):
      if nums_check(nums) == True:
            break
      elif nums[0] >= nums[1]:
            nums[1] *= 2
      elif nums[1] >= nums[2]:
            nums[2] *= 2

print("Yes") if nums_check(nums) == True else print("No")