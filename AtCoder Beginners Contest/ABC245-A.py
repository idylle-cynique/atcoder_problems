'''ABC245 - A
    問題のような大きさ比較は、0埋めさえ適切に行えば文字列比較でも実現可能
    したがって、基本的な回答は0埋め処理を施した時刻文字列を生成し比較をする
    というやりかたになる
    
    ただし、より実践的なやり方で時刻の遅い早いを比較するなら
    datetimeライブラリのようなものを使ってオブジェクトベースで
    比較処理を行う方が、処理の実態が分かり易く、他の処理を加える場合の
    追加処理も容易なので好ましい
'''

from datetime import time

def old_answer():   # 古い解
    A,B,C,D = map(int,input().split())
    A = "{:0=2}".format(A)
    B = "{:0=2}".format(B)
    C = "{:0=2}".format(C)
    D = "{:0=2}".format(D)

    Takahashi = A+B+"00"
    Aoki = C+D+"01"
    #print(Takahashi,Aoki)

    if Takahashi < Aoki:
        print("Takahashi")
    else:
        print("Aoki")
    exit()
    

A,B,C,D = map(int,input().split())

takahashi_time = time(A,B,0)
aoki_time = time(C,D,1)

if takahashi_time < aoki_time:
    print("Takahashi")
else:
    print("Aoki")