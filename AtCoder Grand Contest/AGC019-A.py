# AGC019 - A

# 解説AC問題
# 要求値 N が整数値であることに気付けないと、問題がかなり複雑になってしまう

q,h,s,d = [int(x) for x in input().split()]
n = int(input())

a = min(q*4,h*2,s)      # 要求値はすべて整数なので、1L分の購入には、q,h,lのうちもっとも単価の安いものを選べばよい
b = d

if a*2 < b or n == 1:   # 1L*2本の方が安いのなら、常にそちらを買えばよい
      print(n*a)
else:                   # 2L単位で買った方が安いのなら、可能な限りそちらを使う
      if n%2 == 0:
            print(n*b//2)
      else:
            print(a + ((n-1)//2*b))