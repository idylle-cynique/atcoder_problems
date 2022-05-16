''' ABC251 - B
    本番では下記のTLE回答を提出してしまったが、
    組み合わせ列挙モジュールや動的な配列生成(listのappend,pop)を用いないようにするだけで
    アルゴリズムに改良を加えなくとも十分高速に計算できることが分かったので改めて書き直した
    改良点は以下の通り

        1) itertoolsの組み合わせ列挙は用いない(forループを用いるだけで全探索自体はする)
        2) 「良い整数」リストはappendを用いて動的に要素追加を行うのではなく
           「インデックスに対応する整数が良い整数なのか」を真理値で管理するリストを
           事前に指定された長さ(W)で用意し、真理値の変更によって良い整数リストを管理する
        3) 個別に通常ループ、2重ループ、3重ループを回すのではなく、3重ループの中で
           2重ループ、通常ループも完結するようにループ処理を一括化する

    これにより、tle_answer()実行時より大幅に処理速度が上昇し、10倍超処理速度が短縮
    事前にリストの長さを確定させたことでメモリ占有量も1/5未満に収まっている

    今回のテクニックはプログラミング言語問わずすべての言語で応用可能なので、以後は
    可能な限りこの方法を用いるのが好ましいだろうと思われる
'''
def tle_answer():
    import itertools 

    N,W = map(int,input().split())
    Weights = [int(x) for x in input().split()]

    get3 = list(itertools.combinations(Weights,3))
    get2 = list(itertools.combinations(Weights,2))

    goodnumbers = set()

    for i in range(1,3+1):
        combinations = list(itertools.combinations(Weights,i))
        
        for combi in combinations:
            number = sum(combi)
            if number <= W:
                goodnumbers.add(sum(combi))
    print(len(goodnumbers))
        

N,W = map(int,input().split())
Weights = [int(x) for x in input().split()]
goodnumbers = [False for _ in range(W+1)]

for i in range(0,N):
    a_weight = Weights[i]
    if a_weight <= W:
        goodnumbers[a_weight] = True
        
    for j in range(i+1,N):
        b_weight = Weights[j]     
        if a_weight+b_weight <= W:
            goodnumbers[a_weight+b_weight] = True
            
        for k in range(j+1,N):
            c_weight = Weights[k]
            if a_weight+b_weight+c_weight <= W:
                goodnumbers[a_weight+b_weight+c_weight] = True

            #print(a_weight,b_weight,c_weight)


answer = 0
for n,val in enumerate(goodnumbers):
    if val:
        answer += 1
print(answer)