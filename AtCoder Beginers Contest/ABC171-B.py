# ABC171-B
n,k = [int(x) for x in input().split()]
fs = [int(x) for x in input().split()]
fs_s = sorted(fs)
price = 0

for i in range(k):
    price += fs_s[i]
print(price)