# UNICORNプログラミングコンテスト (ABC225) - D

'''
D問題ではあるが、問題で要求されているものをそのまま実装するだけでよい問題
各車両の連結・分離はポインタの発想で線形リストを拡張して前部・後部の接続情報を記録する領域を加えた
二次元リストとして取り扱うことで要求内容を実装できる

そのほかquery = 3の際の出力処理の実装にはやや注意が必要
問題文で強調されているように、クエリ3で与えられた番号が連結車両の先頭であるとは限らないので
与えられた番号を基に先頭車両の番号を確認し、そこから出力できるように処理を工夫する必要がある
なお、この部分の処理はこのコード中のcheck_linking関数で実現させている
'''
from collections import deque

N,Q = map(int,input().split())
Trains = [[i,None,None] for i in range(N+1)] # [車両番号, 前部の車両番号情報, 後部の車両番号情報]という構成
front,back = 1,2 # 可読性を高めるために意図的に別途変数を用意した

def check_linking(idx):
    '''
    リストでも実装可能ではあるが、Pythonの処理速度の問題を考慮してキューによる実装としている
    この場合車両番号整列のためのリスト反転処理が発生しないので最大で2倍程度高速な処理が可能となる
    '''
    queue = deque([str(idx)])
    
    i = idx
    while(Trains[i][front] != None): # 先頭車両(前部情報がNoneの車両)が得られるまで探索
        queue.appendleft(str(Trains[i][front])) # 得た車両番号をキューの先頭に格納
        i = Trains[i][front]
    start = i
    
    i = idx
    while(Trains[i][back] != None):  # 最後部車両(後部情報がNoneの車両)が得られるまで探索
        queue.append(str(Trains[i][back]))      # 得た車両番号をキューの末尾に格納
        i = Trains[i][back]
    end = i
    
    return list(queue) # リスト化したものを返す

for _ in range(Q):
    query = list(map(int,input().split()))
    #print("command:",query[0])
    if query[0] == 1:
        x,y = query[1:]
        Trains[y][front] = x
        Trains[x][back] = y 
    elif query[0] == 2:
        x,y = query[1:]
        Trains[y][front] = None
        Trains[x][back] = None
    else: # クエリ3の処理
        output_list = check_linking(query[1]) # check_linking関数で出力する車両番号リストを得る
        print(str(len(output_list)) + " " + " ".join(output_list))