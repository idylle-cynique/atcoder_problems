# ABC140 - C

# 解となる数列を得るには、B_i >= max(A_i,A_i+1)と逆のことをすればよい
# 数列Bを反転させて、A[0] = B[0]としたあと、min(B[i],B[i+1])を順番に数列Aに格納していく

N = int(input())
b = [int(x) for x in input().split()]
b = b[::-1]
a = [b[0]]
total = b[0]
#print(b)

if N-1 == 1 or N-1 == 2: # コーナーケース(1)
    total += b[-1]
    print(total)
    exit()
    
if N-1 == 2: # コーナーケース(2)
    total += (min(b)+b[-1])
    print(total)
    exit()
    
for i in range(N-1-1):
    #print(b[i],b[i+1]); print(a)
    a.append(min(b[i],b[i+1]))
    total += min(b[i],b[i+1])

total += b[-1]

print(total)#; print(a) 