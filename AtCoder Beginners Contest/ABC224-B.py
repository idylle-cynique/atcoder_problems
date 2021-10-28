# ABC224 - B

'''
問題文で要求されている通りに実装を行えばよい
4重ループ処理を行うので計算量はO(N^4)であるが、具体的なループ回数は最大50^4 = 6,250,000回で
pythonでも十分高速に処理できる程度に収まる
'''

H,W = map(int,input().split())
A = [[int(x) for x in input().split()] for y in range(H)]

for i_1 in range(H):
    for i_2 in range(i_1+1,H):
        for j_1 in range(W):
            for j_2 in range(j_1+1,W):
                #print(i_1,j_1,":",i_2,j_2)
                if A[i_1][j_1]+A[i_2][j_2] <= A[i_2][j_1]+A[i_1][j_2]:
                    pass
                else:
                    print("No")
                    exit()

print("Yes")