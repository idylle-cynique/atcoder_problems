''' ABC264 - C
    サンプル入出力例を元に、問題における条件を満たす行列Bとはどのようなものか
    について考えていくと
    行列Bの行・列中の各要素を番号の小さいものから取り出して並べたときに次のような条件を満たす場合
    問題で要求されている一致化処理が可能だと言えることがわかる
        1.) 並べた行列Bの行要素群が、行列A内の行中のある行要素群の部分集合で、かつその要素間の順序関係が一致する
        2.) 並べた行列Bの列要素群が、行列A内の列中のある列要素群の部分集合で、かつその要素間の順序関係が一致する
        3.) 1.) 2.) の条件が行列B中の全ての行・列において満たされている
        4.) 1.) 2.) の条件を満たすような行列Bの行・列と行列Aの行・列との組が重複することがない
        5.) 上記の条件を満たす行A・行Bを元の成分番号順にしたがって並べたとき、その順序と組とが一致する
        6.) 上記の条件を満たす列B・列Bを元の成分番号順にしたがって並べたとき、その順序と組とが一致する
    
    少々説明が複雑ではあるが、要するに行列Aから行・列を削除した場合の行列では要素数は減っても削除後の
    行・列の順序関係や要素内容が変更されることはない、したがって行列Bの要素内容や順序関係が行列Bの部分だと
    言えるような行列かどうかを判別すれば問題における条件を満たすかどうかを判定することができる……といったような理屈

    概ねざっくりforループを使えば判別が可能だが、次のような単位行列のような行列がコーナーケースとして存在するので注意が必要
        行列A = [2 1
                 1 2]
        行列B = [1 2
                 2 1]
    
    公式解説はbit全探索を用いて行列Aのから問題中の処理を全パターンで試して判別する、といったようなものとなっているが、
    この場合O(2^(H+W))で、最大2^10 = 10^6ものループ処理が発生するため、処理速度としては間に合うが遅く、
    行列の大きさがより大きくなった場合に対応できない

    この解法では対応する行・列の取り出し、および取り出した行・列の比較判定処理がそれぞれ O(N) 程度におさまり断然高速
'''

ha,wa = map(int,input().split())
A = [[int(x) for x in input().split()] for y in range(ha)]

hb,wb = map(int,input().split())
B = [[int(x) for x in input().split()] for y in range(hb)]

def check_row(ar,br)->bool:
    a_row,b_row = A[ar],B[br]
    a,b = 0,0
    for bi in range(len(b_row)):
        for ai in range(a,len(a_row)):
            #print(ai,a_row[ai],":",bi,b_row[bi],"->",a_row[ai] == b_row[bi])
            a += 1
            if a_row[ai] == b_row[bi]:
                break
        else: return False
    return True

def check_col(ac,bc)->bool:
    a_arr,b_arr = list(),list()
    for i in range(ha): a_arr.append(A[i][ac])
    for i in range(hb): b_arr.append(B[i][bc])
    a,b = 0,0
    
    for bi in range(len(b_arr)):
        for ai in range(a,len(a_arr)):
            #print(ai,a_arr[ai],":",bi,b_arr[bi],"->",a_arr[ai] == b_arr[bi])
            a += 1
            if a_arr[ai] == b_arr[bi]:
                break
        else: return False
    return True

row_flag = True
col_flag = True

si,sj = 0,0

for bi in range(hb):
    for ai in range(si,ha):
        rf = check_row(ai,bi)
        if rf: 
            si = ai+1
            break
    else:
        row_flag = False
        break

for bj in range(wb):
    for aj in range(sj,wa):
        cf = check_col(aj,bj)
        if cf: 
            sj = aj+1
            break
    else:
        col_flag = False
        break

#print(row_flag,col_flag)
answer = "Yes" if (row_flag and col_flag) else "No"
print(answer)