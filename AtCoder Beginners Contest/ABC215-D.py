'''ABC215 - D
    問題で求められているような解となる数を直接求めるのではなく、
    「解となり得る数の集合」から「解となり得ない数の集合」を取り除くことで
    「解となる数の集合」を求めよう、というふうに考えてみる。

    「解となり得ない数」とは、gcd(A_i, k) != 1 であるような k
    つまり、「1以外の共通の素因数を持ち得るような数」である
    また、このような数はどういったものか、を考えていくと
        i)   数列Aの要素の約数であるような数
        ii)  数列Aの要素を約数に持つような数
        iii) 1以外の整数 
    であることがわかる。
    あとはこの条件に当てはまるものを集合型で列挙し、整数集合全体との差集合をとればよい
'''

def check_divs(n):
    x = 1
    
    lower_divs = []
    greater_divs = []
    while(x*x <= n):
        if n%x == 0:
            lower_divs.append(x)
            if x**2 != n:     
                greater_divs.append(n//x)
        x += 1
    
    divnums = lower_divs + greater_divs[::-1]
    return divnums

N,M = map(int,input().split())
A = [int(x) for x in input().split()]

divs = set()
not_answer = set() # 解となり得ない数の集合

for ele in A:       # 数列Aの要素の約数であるような整数を列挙する(ただし1は例外)
    for div in check_divs(ele):
        divs.add(div)
    divs.discard(1)

for div in divs:    # 数列Aの要素を約数に持つような整数を列挙する
    i = 1
    while(div*i <= M):
        not_answer.add(div*i)
        i += 1
#print(divs); print(not_answer)

answer = set([int(x) for x in range(1,M+1)]) - not_answer # 整数集合全体との差が解となる

print(len(answer))          # 出力する要素の個数を表示
for n in sorted(answer):    # 解の出力
     print(n)