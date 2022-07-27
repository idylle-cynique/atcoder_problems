''' ABC261 - C
    問題で求められている処理を愚直なループ処理を用いて行うとO(N^2)となり
    制限時間内の処理が実現できないので、何かしらの工夫をしてO(N)に抑えなさい、という問題

    解法自体は至って簡単で、単にO(logN)以下で格納したデータの存在確認と出現回数の参照ができるような
    データ構造を用いて読み出したファイル名の情報を参照しつつ、番号文字列の付加処理を行えばよい

    具体的には辞書型(dict, C++におけるunorderd_map)のことで、
    これを用いることにより線形計算量で上記のような処理が実現できる
'''

N = int(input())
filenames = list(["" for _ in range(N)])
filedict = dict()

for idx in range(N):
    filenames[idx] = input()

for idx in range(N):
    key = filenames[idx]
    filename = filenames[idx]
    
    if key not in filedict:
        filedict[key] = 0
    else:
        filedict[key] += 1
        
    if filedict[key]:
        print(f"{filename}({filedict[key]})")
    else:
        print(filename)
        
