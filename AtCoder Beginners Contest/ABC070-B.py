# ABC070 - B

# 各範囲の下限(a,c)のうち大きい方、上限(b,d)のうち小さい方をとり、その差を求めればよい
# 重なる範囲がない(0)場合、差が負数になるので、max(0,差)として切り上げると一行で書くことができる

a,b,c,d = map(int,input().split())
print(max(0,min(b,d) - max(a,c)))
exit()

# 自分で導出した解答コード
# a,b,c,dの制約の1~100までという範囲に着目して、シミュレートによる解の導出コードとしたが、
# このコードの場合、制約が大きい(1~10**9など)ときTLEになってしまう。望ましい解答ではない
a,b,c,d = map(int,input().split())
ans = 0
ab_set = set()
cd_set = set()

for x in range(a,b):
    ab_set.add(x)
    
for x in range(c,d):
    cd_set.add(x)

#print(ab_set);print(cd_set); print(ab_set&cd_set)
print(len(ab_set&cd_set))