''' ABC221 - D
    ログイン日時として把握すべき日時が1～10^9日までと非常に大きいため
    各日にちにおけるログイン者数の情報を格納するような実装はできない

    ただ、制約に示されているように総プレイヤー数は2*10^5人と比較的少ないので
    各プレイヤーのログイン・ログアウト日情報だけをもとに各期間における
    オンラインユーザ数を計算するのであれば、十分高速に機能する

    この問題ではただ単に各日におけるオンラインユーザ数のみを把握しておけばよいので
    各ユーザのログイン日ログアウト日を固有のものとして取り扱う必要はなく
        「A_i日にオンラインユーザ数が1増え, B_i日にオンラインユーザ数が1減った」
    とだけ解釈すればよい

    ならばログイン日、ログアウト日をまとめたリストを用意して日にちで昇順にソートし
    順番にオンラインユーザ数の増減を記録していくとともに、あるログイン・ログアウト日から
    次のログイン・ログアウト日までの間のオンラインユーザ数を辞書やリストなどに記録していき
    最後に記録したコンテナの中身を出力してやればよい
'''

N = int(input())
Data = dict()
Data_list = list()

for i in range(N):
    a,b = map(int,input().split())
    b = a+b
    Data[a] = +1 if a not in Data else Data[a]+1
    Data[b] = -1 if b not in Data else Data[b]-1

for k,v in Data.items():
    Data_list.append([k,v])
    
Data_list.sort()
#print(Data); print(Data_list)

predate,prelog = 0,0
cnt = 0
Login_data = [0] * (N+1)

for data in Data_list:
    #print(data)
    date,log = data
    
    Login_data[cnt] += (date-predate)
    cnt += log
    predate,log = date,log

print(" ".join([str(x) for x in Login_data[1:]]))