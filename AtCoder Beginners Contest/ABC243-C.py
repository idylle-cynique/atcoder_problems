# ABC243 - C

'''
    即座に思いつくのは、入力値から2人選ぶ組み合わせを全パターン列挙し
    衝突が発生するものが存在するかしないか試す、というものだが、
    制約をベースに組み合わせパターンの最大値を考えると
    (2*10^5)*(2*10^5-1)//2 ≒ 2*(10^10) と 数秒程度では到底計算が間に合わなくなる

    衝突が発生する場合とはどのような場合なのか、を考え無駄な処理を省く必要がある
    図などを書いて問題を整理していくと衝突が発生するのは次のような条件を満たす2点(2人)
    の場合だけであることがわかる

        i)  Y座標の値がいずれも同じである
        ii) 右側に進む(S_i = 'R')人のいるX座標値が、
            左側に進む(S_i = 'L')人のいるX座標値よりも小さい
    
    つまり、衝突するかしないかを調べる必要のある組み合わせは、
    Y座標が等しい2点の組み合わせに限られる、ということになる

    しかし、X,Yの値として取り得る値の範囲は0～10^9と広いので、
    これだけではまだ次のような場合に膨大な組み合わせが発生してしまう

        ex.) Y座標値がすべて同じで、X座標値だけが異なる2*10^5個の座標が入力値として与えられたとき
    
    なので、ここの部分についても無駄な処理を省きたい
    衝突の発生条件として示したうちの(ii)を整理するとわかるが、
    たとえばY座標値が同じでX座標値だけ異なる座標の組み合わせとして
        S_i = R であるもので、Xの座標が1,3,7
        S_i = L であるもので、Xの座標が2,10
    というような場合、組み合わせとしては3×2 = 6通りあるが、全て試さなくても
    S_i = Rであるもののうち最も左にあるものとS_i = L であるもののうち最も右にあるもの
    の2つにおいて衝突が発生しないなら、ほかのどの組み合わせでも衝突は発生し得ない
    逆に、このときに衝突が発生するならば、他の組み合わせでも当然衝突は発生するともいえる
    つまりS_i = R,L別に座標を選り分け、さらにそこからY座標値が等しいもののうち
    最も左側(Xの値が小さいもの), 最も右側(Xの値が大きいもの)だけを記録していき
    選り分けたものだけ衝突検証を行えばよい

    この場合、全ての入力座標のY座標が異なり、またそれらに対応する
    逆向きに進むような座標が存在する場合でも、10^5個の比較、つまりO(N)だけの処理で
    解答を得ることができる
'''

N = int(input())
Coordinates = [list(map(int,input().split())) for x in range(N)]
Courses = list(input())
collision = "No"

# Y軸の値が同じ向きが →←の関係の値が存在するとき衝突が発生する
# 右向きに進む人たちと左向きに進む人たちとを選り分け、Y座標を比較していけばよい

fltr_dict = {}
frtl_dict = {}

for i in range(N):
    c = Courses[i]
    x,y = Coordinates[i] 
    if c == "R": # 右に向かって進む人たちの情報を整理
        #print(c,":",x,y)
        if y in fltr_dict: # Y座標値が同じ人たちがいる場合
            if fltr_dict[y] > x: # X座標値が最も小さいものだけ記録しておけばよい
                fltr_dict[y] = x
        else:              # 新規に情報を追加
            fltr_dict[y] = x
            
    else:        # 左に向かって進む人たちの情報を整理
        
        if y in frtl_dict:
            if frtl_dict[y] < x: # X座標値が最も大きいものだけ記録しておけばよい
                frtl_dict[y] = x
        else:              # 新規に情報を追加
            frtl_dict[y] = x
            
#print(fltr_dict); print(frtl_dict)

for k,v in fltr_dict.items():
    #print(k,v)
    if k in frtl_dict: # 右に向かって進む人たちと左に向かって進む人たちで、Y座標が等しい組みあわせが存在するか
        #print(k,":",fltr_dict[k],frtl_dict[k])
        
        if fltr_dict[k] < frtl_dict[k]:
            collision = "Yes"
            print(collision)
            exit()

print(collision)