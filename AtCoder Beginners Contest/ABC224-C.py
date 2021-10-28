# ABC224 - C

'''
公式解説による解法は、三角形になる組み合わせであれば常に三点からなる図形の面積が正の面積値をとるという点
に着目して、最大300^3の全探索を行うというものだったが、ここでは異なる解法をとっている

「どのような3点なら三角形になるのか」ではなく、逆に「どのような3点だと三角形にならないのか」を考えると
それは「3点を結んだ時にちょうどまっすぐな線分になるとき」であり「三角形を成す3つの線すべての傾きが同じであるとき」
である、ということがわかる。
これをもとにitertoolsモジュールを用いて与えられた座標の組み合わせとして有り得るものを全列挙し、
順番に上記の条件を満たすかどうかをチェックした。
このとき3点がX軸やY軸に平行な場合Xの変化量が0となってゼロ除算が行われてしまったりするためこれらを避けるようさらに
別途条件式を追加している

なお、この場合のループ処理回数は最大で300*299*298/3*2*1 = 4,455,100回であり、
300^3 = 27,000,000回の愚直な全探索よりも定数倍高速に処理が可能となる
'''
import itertools

def calc_nCr(n,r): # 組み合わせ数の試算
    r = min(n-r,r)
    numer = 1
    denom = 1
    for i in range(n,r,-1):
        numer *= i
        denom *= (n-i+1)
    #print(numer,"/",denom)
    return numer//denom

def check_parallel(a,b,c): # 3点をつないだ線がX軸ないしY軸に平行でないかチェック
    if a==b and b==c:
        return True
    else:
        return False
    
N = int(input())
Coordinates = [list(map(int,input().split())) for _ in range(N)]
Combinations = list(itertools.combinations(Coordinates,3))
cnt = 0
#print(calc_nCr(len(Coordinates),3)) print(Coordinates); print(len(Combinations),":",Combinations)

for elements in Combinations:
    #print(elements)
    x_1,y_1 = elements[0]
    x_2,y_2 = elements[1]
    x_3,y_3 = elements[2]
    
    if check_parallel(x_1,x_2,x_3) == True or check_parallel(y_1,y_2,y_3) == True: # 3点を結んだ3つの線がX,Y軸に平行でないか
        continue # 平行なら三角形にならないので以下の処理はせずに終了
    
    if x_2-x_1==0 or x_3-x_2==0 or x_1-x_3==0: # (X軸,Y軸に平行でない3点の組み合わせのうち)Xの変化量が0である2点が含まれていないか
        cnt += 1 # 全ての線分がX,Y軸に平行でなく、一部の線分だけX軸に平行ならば、それは全ての線分の傾きが等しくはならいので三角形になると言える
        continue
    else:                         # そうでないなら条件式を傾きを求める
        m_1 = (y_2-y_1)/(x_2-x_1)
        m_2 = (y_3-y_2)/(x_3-x_2)
        m_3 = (y_1-y_3)/(x_1-x_3)
        #print(m_1,m_2,m_3)
        if m_1==m_2 and m_2==m_3: # 各線の傾きが等しいなら三角形にならない      
            continue
        else:                     # 等しくないなら三角形になる
            cnt += 1
        
print(cnt) #解を出力