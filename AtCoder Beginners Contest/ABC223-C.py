# ABC223 - C

'''
解説では上手く数式にまとめられていたが、自分では本番中に数式にまとめることが出来なかったので、
そのままシミュレーションをベースに解を求めた

左右から付けた火が衝突し導火線が燃え尽きるのは、左右いずれか一方から着火し
もう一方の端に到達するまでの時間の半分なので、まず左右の火が衝突する時間を求め、
そこから左から着火された火が右から来た火と衝突するまでに伝っていく導火線の距離を求めていく、という流れとなっている
'''

N = int(input())
A = []
B = []
times = [0]
for i in range(N): 
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)

for i in range(N): # 左端から着火していった時に、各導火線を燃やし尽きるタイムを記録
    times.append(times[-1] + (A[i]/B[i]))

times = times[1:]  # 開始時間は取り除く
answer = 0
endtime = times[-1]/2 # 左右の火が衝突する時間

for i in range(N): # 各導火線までの到達タイムリストをもとに衝突時間までの到達距離をシミュレート
    if times[i] <= endtime: # 左からi番目の導火線の到達時間が衝突時間以下なら、その導火線の距離をそのまま加算
        #print(answer,":",endtime, times[i],i)
        answer += A[i]
        
    else:                   # そうでないなら、衝突するまでの残り時間で到達できる距離を求め、その分だけ加算
        if i == 0: # 例外処理(先頭の導火線を伝っている途中に衝突する場合の処理)
            answer = endtime * B[0]
            break
        else:      #
            overtime = times[i] - endtime # i番目の導火線を燃やし尽くすまでにかかる時間から実際の衝突時間を差し引いて、超過時間を求める
            #print(overtime); print(times[i],"::",endtime,B[i])
            answer += A[i] # そのままi番目の導火線の距離を加算
            answer -= (overtime * B[i]) # うち、超過して加え入れた分の距離を超過時間をもとに計算し、差し引く
            break # ループ処理終了

print(answer)