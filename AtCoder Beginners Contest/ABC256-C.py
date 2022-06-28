''' ABC256 - C
    条件を満たす値の並び方を全探索していく場合、
    3×3のマスに対して1～30までの値を代入してそれぞれに検証していく、といったような
    完全に愚直な探索の場合、30^9で2*10^13ものループ処理が発生し、処理が間に合わない

    したがって、条件を満たす値の並び方についてもう少し整理し、
    探索する値の幅や探索するマスの数を削減したい

    サンプル入出力例などをもとに改めて探索する値の幅について考えてみると
    次のことが言えることがわかる
        i)  縦ないし横に並んだ数値の和は(当然だが)それに対応する入力値の和を超えてはいけない
            ということなので、並んでいる3つのマスのうち、2つまで確定すれば残りのマスに入る値
            は自動的に決定する(したがって、2つのマスまで列挙すればよいことになる)
        ii) また縦2列ないし横2行のいずれかの値が確定すれば、残っている1列および1行の値についても
            i)と同じ理屈で自動的に決定される
    すると、ループによる全列挙が必要なのは、実際のところ9マスの内4マスだけでよい、ということになる

    この場合30^4≒10^6程度のループ処理回数の列挙で済み、それぞれのパターンについて条件を満たすかの
    検証を行いひとつずつ数え上げを行っても、十分高速に処理が可能となる

'''
h1, h2, h3, w1, w2, w3 = map(int,input().split())

combi_h1 = list()
combi_h2 = list()
answer = 0

for i in range(1,h1+1):
    for j in range(1,h1+1):
        k = h1 - i - j
        
        if(k > 0):
            combi_h1.append([i,j,k])
            
for i in range(1,h2+1):
    for j in range(1,h2+1):
        k = h2 - i - j
        
        if(k > 0):
            combi_h2.append([i,j,k])
            
widths = [w1,w2,w3]

for combi1 in combi_h1:
    for combi2 in combi_h2:
        combi3 = list()
        for i in range(len(combi1)):
            #print(":", combi1[i], combi2[i])
            c3 = widths[i] - combi1[i] - combi2[i]
            combi3.append(c3)
        
        sum_c3 = 0
        for c3 in combi3:
            if c3 <= 0:
                break
            sum_c3 += c3
        else:
            if sum_c3 == h3:
                #print(combi1,combi2,combi3)
                answer += 1
            
print(answer)