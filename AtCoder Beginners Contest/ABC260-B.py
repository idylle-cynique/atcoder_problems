''' ABC260 - B
    一番簡単な解法は、問題で求められている処理を
    直接一連の値が格納されたリスト内の要素の探索・削除をひとつずつ行い求めていく、というもの

    O(N^2)の非常に計算効率の悪い処理になるが、ここではNの値が最大でも1000というふうに条件付け
    が成されているため、この計算量でも制限時間内での計算は可能

    ただし、当然ながら実際の開発の現場でこうした粗雑な実装を行うのはまずいので、
    ソートを用いてある程度現実的な計算量で実装したい

    ここではoperatorモジュールのitemgetter関数を用いて
        [生徒番号, 数学の得点*(-1), 英語の得点*(-1), 二科目の合計得点*(-1)]
    といったような様式で格納されている得点リストを、基準となるキーに応じてソートし
    
    これを参照しつつ合格者番号をset(集合)に格納していくことで
    X人,Y人,Z人の合格者をそれぞれ線形計算量程度で求めている

    格納する一連の得点値を負数に直しているのは、問題における
    「同じ得点のものがいる場合は生徒番号の小さいものを優先する」
    という条件の通り、得点リストにおける生徒番号と得点値とを昇順ベースでソートできるようにするため

    ここでの一連の処理は
        i)  各キーに応じたソート処理 O(N・logN)
        ii) 数学、英語、二科目の合計得点に応じた合格者の抽出 O(N)
    全体での計算量は i) より O(N・logN)
'''

from operator import itemgetter

N,X,Y,Z = map(int,input().split())
score_list = [list() for _ in range(N)]
math_list = [int(m) for m in input().split()]
eng_list = [int(e) for e in input().split()]
successful_applicants = set()

for i in range(N):
    score_list[i] = [i+1,(-1)*math_list[i],(-1)*eng_list[i],(-1)*(math_list[i]+eng_list[i])]

x,y,z = 0,0,0
score_list = sorted(score_list, key=itemgetter(1,0)); #print(X,":",score_list)
for i in range(N):
    if x == X: break
    if score_list[i][0] not in successful_applicants:
        successful_applicants.add(score_list[i][0])
        x += 1

score_list = sorted(score_list, key=itemgetter(2,0)); #print(Y,":",score_list)
for i in range(N):
    if y == Y: break
    if score_list[i][0] not in successful_applicants:
        successful_applicants.add(score_list[i][0])
        y += 1

score_list = sorted(score_list, key=itemgetter(3,0)); #print(Z,":",score_list)
for i in range(N):
    if z == Z: break
    if score_list[i][0] not in successful_applicants:
        successful_applicants.add(score_list[i][0])
        z += 1

for ans in sorted(successful_applicants):
    print(ans)