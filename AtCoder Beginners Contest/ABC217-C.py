''' ABC217 - C
    数列の逆置換処理を求める問題
    解法については特に工夫は要らず、そのまま問題の要求通りの実装を行えばよい
'''

N = int(input())
Ps = [int(x) for x in input().split()]
R = []
Answer = []

for i in range(N):
    #print(str(Ps[i]) + "番目の要素が" + str(i+1))
    R.append([Ps[i],i+1])
    
R = sorted(R,reverse=True)
#print(R)

while(R):
    ele = R.pop()
    Answer.append(ele[1])

print(" ".join([str(ele) for ele in Answer]))