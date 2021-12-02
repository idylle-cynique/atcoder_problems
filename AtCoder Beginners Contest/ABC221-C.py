# ABC221 - C

'''
数字Nから各桁の番号を選り分けて得られる2つの数字をA,Bとすると、
Aに入れる桁を0, Bに入れる桁を1(Not 0)と考えてbit全探索を適用すれば
A,Bとして並べられ得る数字の全グループ分けが可能となる

また、グループ分けしたあとに、AとBの積をとった時に最も大きな値となる数字の並びはあらかじめ決まっているので
ここからさらにそれぞれ順列を生成して全パターン試す必要はない

    例えば、A = {1,2,3}, B = {0,4}のような場合で全部試すと
    123*40,132*40,213*40,231*40,312*40,321*40の6パターンがあり、最大は321*40である
    ここから見ればおよそ推測できるように、どのようなグループ分けが成された場合でも
    「大きな数字を大きな桁に、小さな数字を小さな桁に持って行って得られる数字同士の積が最も大きな値をとる」
    ということがわかる

計算量はbit全探索にかかる分、すなわちO(2^(|Nの長さ|))となる
'''

N = input()
length = len(N)
Answer = 0

for i in range(1,2**length-1): # 00000,11111となるような場合は候補として取り除いておく
    A = []
    B = []    
    for j in range(length):
        #print((i>>j)&1)
        if (i>>j)&1 == 1:
            A.append(N[j])
        else:
            B.append(N[j])

    A_num = int("".join(sorted(A,reverse=True)))
    B_num = int("".join(sorted(B,reverse=True)))
    #print("".join(sorted(A,reverse=True)),":","".join(sorted(B,reverse=True)))
    #print(A_num,":",B_num)
    Answer = max(Answer,A_num*B_num)

print(Answer)
    
    
        
        