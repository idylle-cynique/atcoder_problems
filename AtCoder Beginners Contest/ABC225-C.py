''' ABC225 - C
    実際にシミュレートして入力値が期待される様式を満たしているかどうかチェックすればよい
    制約は最大で10000行4列(40000要素)程度なので、
    そのまま処理内容を再現しても十分高速に機能する

    ただし、ただ単に各要素の値の妥当性検査を行えば良いわけではなく、
    矩形(長方形)領域の列位置の上下関係が適正かまで考慮に入れること
    例えば
         7  8  9 10
        14 15 16 17
    のような入力値は条件を満たすように思えるが、実際のカレンダー上では下のようになっている
                            7
          8  9 10          14
         15 16 17 
    この場合矩形領域とは言えないので、こうしたケースも考慮してコードを書く必要がある
'''

N,M = map(int,input().split())
B = [[int(x) for x in input().split()] for y in range(N)]
idx_locate = (B[0][0]+6)%7
#print(idx_locate+M,":",7)

if idx_locate+M > 7:
    print("No")
    exit()

for i in range(N):
    if i == 0:
        for j in range(1,M):
            #print(B[i][j-1],":",B[i][j]-1)
            if B[i][j-1] != B[i][j]-1:
                print("No")
                exit()
        if N == 1:
            break
    else:        
        for j in range(M):
            #print(B[i][j]-7,":",B[i-1][j])
            if B[i][j]-7 != B[i-1][j]:
                print("No")
                exit()

print("Yes")
            