# ABC154 - D

n,k = map(int,input().split())
dices = [int(x) for x in input().split()]
expected_values = []

for i in dices: # 各ダイスの期待値はa_1 = 1で等差が1であるdices[i]個の数列の総和の平均と考えられる
    tmp = ((i+1)*i)/2/i 
    expected_values.append(tmp)

#print(n,k); print(dices); print(expected_values)
ans = tmp = sum(expected_values[:k])

for i in range(k,n): #尺取り法でよく用いる方法で区間内の総和をO(n)で求めていく
    #print(expected_values[i-k],expected_values[i])
    tmp = tmp - expected_values[i-k] + expected_values[i]
    ans = max(ans,tmp)

print(ans)