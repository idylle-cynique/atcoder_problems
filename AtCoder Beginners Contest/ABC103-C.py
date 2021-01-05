#ABC103 - C

# 数学的とんち問題の類
# 各要素の余りの最大値はいずれもa_i-1なので、それらを全部足し合わせて行けば自ずと解答値が得られる 

n = int(input())
a = [int(x) for x in input().split()]

total = 0
for i in a:
      total += i

print(total - n)
