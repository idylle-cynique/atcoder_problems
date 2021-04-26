# AGC017 - A

# パッと思い浮かぶのはbit全探索による全探索だが、クッキーリストの要素数が最大50個とあるので
# 最大で2^50 ≒ 10^15 ものループ処理が発生することになる。当然ながらこれでは処理が間に合わない

# p の条件を要約すると、選んだ要素のクッキーの数の総和が偶数になるようにしたり奇数になるようにしたりしてほしい、ということなので
# 偶数(個のクッキー)が入っている要素と奇数(個のクッキー)が入っている要素とを選り分け、それぞれから何個の要素を取り出すか、を全探索すれば
# p の条件を満たす袋の選び方が分かる。組み合わせは具体的に要素を列挙する必要はなく組み合わせ数を求めるだけでよいので、簡単な計算処理で済む

def calc_combi(n,r): # N個の中からr個の選ぶときの組み合わせの数を求める
    numer = 1 # 分子
    denom = 1 # 分母
    
    for i in range(r):
        #print(n-i,"/",(i+1))
        numer *= (n-i)
        denom *= (i+1)
    
    return numer//denom

n,p = map(int,input().split())
cookies = [int(x) for x in input().split()]
evens,odds = [],[]
ans = 0

for c in cookies: # クッキーリストを偶数個入っている袋(要素)、奇数個入っている袋(要素)とに選り分ける
    if c%2 == 0:
        evens.append(c)
    else:
        odds.append(c)

e = len(evens)
o = len(odds)
#print(e,":",evens); print(o,":",odds)

for ei in range(e+1):
    for oi in range(o+1):
        mod = ((2*ei)+oi)%2
        #print(ei,oi,"=",mod)
        
        if mod == p: # 条件を満たすとき
            if ei == 0: # 偶数数列の中からei個の偶数を選ぶときの候補数を求める
                combi_e = 1
            else:
                combi_e = calc_combi(e,ei)
            
            if oi == 0: # 奇数数列の中からoi個の奇数を選ぶときの候補数を求める
                combi_o = 1
            else:
                combi_o = calc_combi(o,oi)
            
            # (偶数要素の選び方の数) * (奇数要素の選び方の数) が ei個の偶数, oi個の奇数を選ぶときの組み合わせ数
            ans += (combi_e*combi_o)

print(ans)