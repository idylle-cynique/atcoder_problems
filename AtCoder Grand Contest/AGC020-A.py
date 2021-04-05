# AGC020 - A

# 実際にシミュレートしてみると、ゲーム開始時点でのA-B間の距離によって既に勝敗が決していることが分かる。

n,a,b = map(int,input().split())

if abs(a-b-1)%2 == 0:
    print("Borys")
else:
    print("Alice")