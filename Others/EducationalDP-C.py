# Educational DP Contest - C
N = int(input())
A = [0]
B = [0]
C = [0]

for i in range(N):
    a,b,c = map(int,input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    
dp = [[0] * (N+1) for _ in range(3)]

def view_dp(dp_list):
    for row in dp_list:
        print(row)
    print()
    return True

a,b,c = 0,1,2
for i in range(1,N+1):
    #print(A[i],B[i],C[i])

    # i日目にAに行ったときの幸福度の最大値は
    # (1) i-1日目にBに行ったときに得られた幸福度 + i日目にAに行ったことで得られた幸福度
    # (2) i-1日目にCに行ったときに得られた幸福度 + i日目にAに行ったことで得られた幸福度
    # の二つのうちのより大きな値 
    dp[a][i] = max(dp[b][i-1]+A[i], dp[c][i-1]+A[i])
    
    # B_iに行ったときの幸福度の最大値
    # (1) i-1日目にCに行ったときに得られた幸福度 + i日目にBに行ったことで得られた幸福度
    # (2) i-1日目にAに行ったときに得られた幸福度 + i日目にBに行ったことで得られた幸福度
    # の二つのうちのより大きな値 
    dp[b][i] = max(dp[c][i-1]+B[i], dp[a][i-1]+B[i])
    
    # C_iに行ったときの幸福度の最大値
    # (1) i-1日目にAに行ったときに得られた幸福度 + i日目にCに行ったことで得られた幸福度
    # (2) i-1日目にBに行ったときに得られた幸福度 + i日目にCに行ったことで得られた幸福度
    # の二つのうちのより大きな値 
    dp[c][i] = max(dp[a][i-1]+C[i], dp[b][i-1]+C[i])

# view_dp(dp)
answer = max(dp[a][N],dp[b][N],dp[c][N])
print(answer)