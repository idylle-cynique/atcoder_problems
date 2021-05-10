# AISING2020 - A

# 想定される入力値が小さいので、そのまま問題文の通りに実装するだけでよい。
# L,Rの値がきわめて大きな値が入る可能性も想定する場合には、
# ループではなくO(1)で算出可能な数式が作れないか考えるのがよい

l,r,d = [int(x) for x in input().split()]
nums = [int(x) for x in range(l,r+1)]
ans = []

for i in range(len(nums)):
      if nums[i]%d == 0:
            ans.append(nums[i])

print(len(ans))