# AISING2020 - B

# 問題文の通りに実装すればよい
# ここではリストによる実装としたが、set型を用いて集合演算を行う方が
# 制約が大きくなっても変わらず高速に処理できるため望ましい

n = int(input())
nums = [int(x) for x in input().split()]
nums_v2 = [] # 一番目の条件を満たすマスを格納
nums_v3 = [] # 二番目の条件を満たすマスを格納

for i in range(len(nums)): # マスの番号が奇数であるものだけを抜き出す
      if (i+1)%2 == 1:
            nums_v2.append(nums[i])

for i in range(len(nums_v2)): # マスに書かれた番号が奇数であるものだけを抜き出す
      if nums_v2[i]%2 == 1:
            nums_v3.append(nums_v2[i])

print(len(nums_v3))