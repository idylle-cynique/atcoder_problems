''' ABC251 - C
    要素の一部に重複する値を含む要素の中から条件を満たすものだけを
    適切に取り出し処理を行うにあたって、どのようにすれば処理速度を悪化させずに
    条件の処理を実装できるか、を問うもの

    パッと思いつくのは文字列と得点の二つの要素を持つ配列を用意し
    都度先行作品(オリジナル)の有無をチェックしていくものだが、
    このチェックを線形探索で行うと都度O(N)の処理となってしまうので
    各要素の処理が間に合わない

    もう少しコンテナのデータ構造について考える必要がある
    ここでは各要素をハッシュで管理しコンテナ内の要素の有無の判定をO(1)で行える
    辞書(連想配列), 集合型などがおあつらえむきで、これを利用することで
    高速にオリジナルな作品だけを抜き出すことができる

    検証はしていないが、文字列でも大小比較は可能なので、
    工夫次第では二分探索(bisect)も利用できるかもしれない
    もちろん、計算量は前者の方が高速
'''

N = int(input())
poemdict = dict()

for i in range(N):
    temp = [str(line) for line in input().split()]
    judge = [i+1, temp[0], int(temp[1])]
    #print(judge)
    itr, string, score = judge
    
    if string not in poemdict:
        poemdict[string] = [i+1,score]
        
max_score = -1
answer_number = 0

for number,score in poemdict.values():
    #print(number,score,":",max_score)
    if score > max_score:
        answer_number = number
        max_score = score

print(answer_number)