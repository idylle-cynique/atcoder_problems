# ABC215 - C

'''
ある文字列中の文字すべて使って得られる文字列を辞書順に並べたときK番目となる文字列を出力する
文字列の長さは最大8なので、 8! = 40320通りが考えられる文字列の数の最大であり、全列挙しても十分処理が間に合う
したがって、並び替えた文字列の重複にだけ注意しつつ、実際に組み合わせをリストアップしていけばよい
ここでは itertools の permutations() と set() を用いて重複を取り除いた順列リストを生成している
'''

import itertools

S,K = map(str,input().split())
K = int(K)

keywords = list(itertools.permutations(S))  # 実際に順列を生成
keywords_set = set(keywords)    # うち、重複しているものを取り除く
keywords_lst = sorted(keywords_set) # 改めて、辞書順にソートされたリストを生成

print("".join(keywords_lst[K-1]))