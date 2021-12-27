# AGC028 - A

# まず、条件を満たす文字列としてあり得る文字列の長さについて考える
# i*(L/N)番目, i*(L/M)番目がいずれも整数番目である必要があることを考えると、必然的に良い文字列の長さは
# 与えられた文字列の長さN,Mの公倍数であり、そのうち最短の長さは最小公倍数lcm(N,M)であると考えることができる
# あとは、実際に与えられた文字列が条件に適合するか、であるが、N,Mの制約上そのまま要求れたとおりに文字列を
# 生成していくことはできない(N=10^5, M=10^5-1のとき、解となる文字列の長さは9999900000ときわめて大きくなる)
# したがって、良い文字列を生成しようとした場合に各文字列のインデックスを求め、
# S,Tの文字列でインデックスが重複するもののうち、入れる必要のある文字列が相異なることがないか、をチェックしてく
# この方法であれば、S,Tの長さ分だけしか探索を要さないため、最大でも10**5回のループで処理を終えることができる

import math

N,M = map(int,input().split())
S = list(input())
T = list(input())
gcd = math.gcd(N,M)
lcm = N*M // math.gcd(N,M)
#print(gcd,lcm)
Sindices = []
Tindices = []

for i in range(N): # 良い文字列Lに対応する文字列Sの各文字のインデックスを計算
    Sindices.append(i*(lcm//N))
    #print(i*(lcm//N))
    
for i in range(M): # 良い文字列Lに対応する文字列Tの各文字のインデックスを計算
    Tindices.append(i*(lcm//M))
    #print(i*(lcm//M))

#print(Sindices); print(Tindices);

i,j = 0,0 # 文字列Sのインデックス, 文字列Tのインデックス
while(i<N and j<M): # どちらか一方の良い文字列用インデックスの探索を終えるまで線形探索
    if Sindices[i] == Tindices[j]:  # 良い文字列にあてはめたいインデックスの値が重複しているとき
        #print(Sindices[i],S[i],"-",Tindices[j],T[j])
        if S[i] == T[j]: # 当てはめたい文字が同じであるときは処理を続行
            i += 1
            j += 1
        else:            # 条件を満たす良い文字列を生成できないので処理終了
            print(-1)
            exit()
    elif Sindices[i] < Tindices[j]: # 文字列Sの良い文字列用インデックスの方が小さい時、インクリメントして次の値に移る
        i += 1
    else:                           # 文字列Tの良い文字列用インデックスの方が小さい時、インクリメントして次の値に移る
        j += 1
        
print(lcm)