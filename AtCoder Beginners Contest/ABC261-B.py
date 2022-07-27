''' ABC261 - B
    問題文中の処理をそのまま実装するだけでよい
    最大でも1000行1000列程度の大きさの行列なので、二重ループを用いても十分高速に処理が可能

    処理内容は線型代数のような内容で、受け取った正方行列(総当たり表)の転置行列成分、
    具体的には(i,j)成分と対応関係にある(j,i)成分とを比較していく、といったようなもの
'''

N = int(input())
roundrobin = []

for _ in range(N):
    roundrobin.append(list(input()))

flag = True
answer = "correct"

for i in range(N):
    for j in range(i+1,N):
        if (i == j) and (roundrobin[i][j] != "-"):
            flag = False
        
        if i != j:
            outcome = roundrobin[i][j]
            if outcome == "W" and roundrobin[j][i] != "L":
                flag = False
                
            if outcome == "L" and roundrobin[j][i] != "W":
                flag = False
                
            if outcome == "D" and roundrobin[j][i] != "D":
                flag = False
            
        if not(flag):
            answer = "incorrect"
            break
    else:
        continue
    break


print(answer)
        
        