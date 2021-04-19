# ARC117 - A

# 神の数列に利用できる値の幅は大きく、要素数は小さい、という点に着目すると、

# a,bのうち大きい方を公差1で長さがaないしbの等差数列とし、
# a,bの小さい方を公差1で長さがa-1ないしb-1の等差数列としたあと、
# 総和が0となるための調整値を与えてやればよい、とわかる

# ここでは制約が 1 <= N <= 1000 であることに着目して、1000~1 までの等差数列を生成させている

a,b = map(int,input().split())

if a >= b: # 正整数要素の数の方が大きい時
    seq_a = [(10**4)-int(x) for x in range(1,a+1)]
    seq_b = [-1*int(x) for x in range(1,b)]
    sum_a = sum(seq_a)
    sum_b = sum(seq_b)
    seq_b.append((sum_a+sum_b)*(-1))
    ans_seq = seq_a+seq_b

else:      # 負整数要素の数の方が大きい時
    seq_a = [int(x) for x in range(1,a)]
    seq_b = [(-1)*(10**4)+int(x) for x in range(1,b+1)]
    sum_a = sum(seq_a)
    sum_b = sum(seq_b)
    seq_b.append((sum_a+sum_b)*(-1))
    ans_seq = seq_a+seq_b

#print(seq_a,"total:",sum_a); print(seq_b,"total:",sum_b)
#print((sum_a+sum_b)*(-1))
print(" ".join([str(ans_seq[i]) for i in range(a+b)])) # 出力
