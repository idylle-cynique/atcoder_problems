# AGC004 - A

# ブロックのうち縦、横、高さいずれのうち一つでも偶数であれば、直方体は条件を満たす形で二等分できる
# すべて奇数からなる直方体の場合、もっとも長い辺をとって、そこからブロックの個数差が1になるように切り出せばよい

block = sorted([int(x) for x in input().split()])

for i in block:
      if i%2 == 0:
            print(0)
            exit()

bigger  = block[0]*block[1] * ((block[2]+1)//2)
smaller = block[0]*block[1] * (block[2]//2)
print(bigger-smaller)