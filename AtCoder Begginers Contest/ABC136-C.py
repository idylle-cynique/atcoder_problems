# ABC136 - C
# 0~iまでの最大値 max_h を記録しておき、max_h > h[i] のとき "No" とすればどうか
# 結果的に上手く実装できず解説AC

n = int(input())
h = [int(x) for x in input().split()]
max_h = h[0]

for i in range(1,n):
      #print(max_h,h[i])
      
      if max_h <= h[i]:
            max_h = h[i]
            continue
      
      if max_h-1 > h[i]:
            print("No")
            exit()

#print(max_h)
print("Yes")