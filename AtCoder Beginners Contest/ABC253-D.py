''' ABC253 - D
    各種値の制約が10^9と非常に大きいので、問題の通りに
    Aの倍数でないもの、Bの倍数でもないものすべてを愚直に全探索し
    数え上げを行うことは出来ない

    ただ、よくよく考えてみると数学における集合の考え方を利用すれば
    直接的に問題の数字を求めずとも、より効率的な計算方法があることがわかる

    数学における包除原理に従えば、
    N以下の整数の集合におけるAの倍数でなくBの倍数でない整数の数
     = N以下の整数の集合の要素数 - (N以下のAの倍数である数の集合の要素数
       + N以下のBの倍数である数の集合の要素数
       - N以下のAの倍数かつBの倍数である数の集合の要素数)
    という形で問題の値を求めることが出来る

    また、やや求めるのに難儀するであろう「N以下のAの倍数かつBの倍数である数の集合の要素数」
    は「”A, B, およびAとBの最大公約数の最小公倍数”の倍数であるN以下の数の集合の要素数」
    という形で計算することができる

    なお、解答コードは多数の変数を用いているが、これは途中の値を確認しながら実装を行った結果
    このようになっただけで、計算式をまとめてしまっても問題はない
'''

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b) 

def lcm(gcdnum,a,b):
    return a*b // gcdnum


N,A,B = map(int,input().split())
total  = ((N+1)*N)//2
lcm_ab = lcm(gcd(A,B),A,B)

div_a = N//A
div_b = N//B
div_lcm = N//lcm_ab
#print(lcm_ab); print(div_a,div_b)

sum_diva = ((div_a+1)*div_a)//2
sum_divb = ((div_b+1)*div_b)//2
sum_lcm = (div_lcm+1)*div_lcm//2
#print(sum_diva,"*",A,":",sum_divb,"*",B,"::",sum_lcm)

total_a = sum_diva * A
total_b = sum_divb * B
total_lcm = sum_lcm * lcm_ab
#print(total_a,total_b,total_lcm)

answer = total - (total_a + total_b) + total_lcm
print(answer)