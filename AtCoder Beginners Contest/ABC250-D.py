''' ABC250 - D
    制約が 1 <= N <= 10^18 と非常に大きいが、条件を満たすp,qの組み合わせのうち、
    最もqの値が大きくなるような組み合わせについて考えてみると、

    N = 10**18 のときの q = 10**6 にやや足りないくらいの値(1は素因数ではないのでp=1にはできない)
    であると予想できる。すると、素数p,qとしてあり得る値は高々10^18の-3乗ということになる

    これくらいまでならエラトステネスの篩を用いれば容易に素数リストを全列挙できる
    また、任意のqに対応するpの値としてあり得るのは、q未満の素数全てとなるので
    素数リストからq未満の要素の個数を二分探索を用いて求める処理を
    条件を満たすqの値全てに対して行い、その総数をカウントしてくことで
    "250に似た数の個数"を求めることができる
'''

import bisect

def elatos(number):
      shieve = [True for x in range(number+1)]
      shieve[0] = False; shieve[1] = False

      n = 2
      while(n**2 < number):
            if shieve[n]:
                  for x in range(2,number//n+1):
                        shieve[n*x] = False
            n += 1

      primes = list()
      for i,v in enumerate(shieve):
            if v:
                  #print(i,v)
                  primes.append(i)
      return primes

N = int(input())

cnt = 0
max_q = int(N**(1/3)//1) # qとしてあり得る値のうちの最大値を求める
primes = sorted(elatos(max_q)) # q未満の素数を全列挙

for q in primes:
    div = min(N//(q**3),q)
    div = min(div,q)

    if div == q: # q**3との商未満の素数を求める(p==qであるようなpは含まない)
        div -= 1
    idx = bisect.bisect_right(primes, div)
    #print(q,":",q**3,div); print(f"-> {idx}?")
    cnt += (idx) # 条件を満たす素数の個数をインクリメント

print(cnt)