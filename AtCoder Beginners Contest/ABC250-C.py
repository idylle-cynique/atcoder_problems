''' ABC250 - C
    基本的には要求されている通りの処理をそのまま実装するだけでよいが
    クエリで要求されている番号のボール位置を求める際に
    そのままリストの線形探索を行ってしまうと、この探索を行うごとに線形計算量がかかり
    Q個のクエリの処理にO(Q), 各クエリでの処理にO(N)かかり、全体でO(N・Q)もの計算量となる
    これでは制限時間内の処理を行うことができない

    指定されたボールの位置を得るために何かしらの工夫をする必要がある
    ここでは辞書型を用いて各ボールの番号とリスト内の位置(インデックス)を管理し
    交換処理と並行してボール位置情報の更新を行うことで
    ボールの位置情報を得るための探索処理をO(1)で完了できるようにしている
'''

N,Q = map(int,input().split())
Queries = [int(input()) for x in range(Q)]

balls = [int(x) for x in range(N+1)] # ある番号が書かれたボールを記録
balldict = dict()                    # 各ボールの位置を記録

for idx, ball in enumerate(balls):
    balldict[ball] = idx

for q in Queries:
    left_idx = balldict[q] # 指定されたボールの位置を得る
    #print(q,left_idx)
    if left_idx+1 < len(balls): # 右隣にボールが存在する場合
        right_idx = left_idx+1
    else:                       # 右隣にボールが存在しない場合
        left_idx -= 1
        right_idx = left_idx+1
    balls[right_idx],balls[left_idx] = balls[left_idx],balls[right_idx] # 指定されたボールを交換
    balldict[balls[right_idx]] =  right_idx # 交換後の位置情報にあわせて辞書を更新
    balldict[balls[left_idx]] = left_idx 
    #print(balls)

answer = [str(ball) for ball in balls[1:]]
print(" ".join(answer))
